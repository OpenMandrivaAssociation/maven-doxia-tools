Name:		maven-doxia-tools
Version:	1.2
Release:	5
Summary:	Maven Doxia Integration Tools

Group:		Development/Java
License:	ASL 2.0
URL:		http://maven.apache.org/shared/maven-doxia-tools/
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-doxia-tools-1.2/
Source0:	%{name}-%{version}.tbz
Patch0:		%{name}-update-interpolation.patch

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	jakarta-commons-io >= 1.4
BuildRequires:	jakarta-commons-logging
BuildRequires:	plexus-utils
BuildRequires:	plexus-interpolation
BuildRequires:	plexus-container-default
BuildRequires:	plexus-i18n
BuildRequires:	maven-shared
BuildRequires:	maven-doxia
BuildRequires:	maven-doxia-sitetools
BuildRequires:	maven2-plugin-compiler
BuildRequires:	maven2-plugin-install
BuildRequires:	maven2-plugin-jar
BuildRequires:	maven2-plugin-javadoc
BuildRequires:	maven2-plugin-resources
BuildRequires:	maven2-plugin-surefire
BuildRequires:	maven-shared-plugin-testing-harness
BuildRequires:	maven-shared-reporting-impl
BuildRequires:	plexus-maven-plugin
BuildRequires:	java-devel >= 0:1.6.0

BuildArch:	noarch

Requires:	jakarta-commons-io >= 1.4
Requires:	plexus-utils
Requires:	plexus-interpolation
Requires:	plexus-container-default
Requires:	plexus-i18n
Requires:	maven-shared
Requires:	maven-doxia
Requires:	maven-doxia-sitetools

Requires:	jpackage-utils
Requires(post):	jpackage-utils
Requires(postun):	jpackage-utils

%description
A collection of tools to help the integration of Doxia in Maven plugins.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
	-Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	-Dmaven.test.skip=true \
	install javadoc:javadoc


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.apache.maven.shared %{name} %{version} JPP %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

