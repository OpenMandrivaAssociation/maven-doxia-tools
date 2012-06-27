Name:		maven-doxia-tools
Version:	1.4
Release:	1
Summary:	Maven Doxia Integration Tools

Group:		Development/Java
License:	ASL 2.0
URL:		http://maven.apache.org/shared/maven-doxia-tools/
Source0:	http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:		%{name}-migration-to-component-metadata.patch

BuildRequires:	apache-commons-io >= 1.4
BuildRequires:	apache-commons-logging
BuildRequires:	plexus-utils
BuildRequires:	plexus-interpolation
BuildRequires:	plexus-container-default
BuildRequires:	plexus-i18n
BuildRequires:	maven
BuildRequires:	maven-shared
BuildRequires:	maven-doxia
BuildRequires:	maven-doxia-sitetools
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-surefire-plugin
BuildRequires:	maven-plugin-testing-harness
BuildRequires:	maven-shared-reporting-impl
BuildRequires:	plexus-containers-component-metadata
BuildRequires:	java-devel >= 1.6.0

BuildArch:	noarch

Requires:	apache-commons-io >= 1.4
Requires:	plexus-utils
Requires:	plexus-interpolation
Requires:	plexus-container-default
Requires:	plexus-i18n
Requires:	maven-shared
Requires:	maven-doxia
Requires:	maven-doxia-sitetools

Requires:	jpackage-utils

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
%patch0 -b .sav


%build
mvn-rpmbuild \
	-Dmaven.test.skip=true \
	install javadoc:aggregate

%install
# jars
install -Dm 644 target/%{name}-%{version}.jar %{buildroot}/%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}

# poms
install -Dpm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc
%doc %{_javadocdir}/*
%doc LICENSE

