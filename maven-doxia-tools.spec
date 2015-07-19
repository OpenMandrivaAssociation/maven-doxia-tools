%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-doxia-tools
Version:        1.6
Release:        2.2
Group:		Development/Java
Summary:        Maven Doxia Integration Tools
License:        ASL 2.0
URL:            http://maven.apache.org/doxia/doxia-tools/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-integration-tools/%{version}/doxia-integration-tools-%{version}-source-release.zip

Patch0:         0001-Port-to-Maven-3-APIs.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-logging-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
A collection of tools to help the integration of Doxia in Maven plugins.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n doxia-integration-tools-%{version}
%patch0 -p1 -b .sav
%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"
%pom_set_parent org.apache.maven:maven-parent:24

%mvn_file : %{name}
%mvn_alias : org.apache.maven.doxia:doxia-integration-tools
%mvn_alias : org.apache.maven.shared:maven-doxia-tools

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Jul 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-2
- Fix org.apache.maven.shared:maven-doxia-tools alias

* Sun Jul 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-15
- Use Requires: java-headless rebuild (#1067528)

* Fri Jan 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-14
- Port to Maven 3 API

* Tue Oct  1 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-13
- Install NOTICE file with javadoc package
- Update to current packaging guidelines
- Fix BuildRequires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11
- Remove test dependencies

* Mon Feb 18 2013 Tomas Radej <tradej@redhat.com> - 1.4-10
- Removed BR on maven-shared (unnecessary + blocking maven-shared retirement)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-8
- Add extra depmap for doxia-integration-tools >= 1.5

* Thu Dec 20 2012 Michal Srb <msrb@redhat.com> - 1.4-7
- Migrated from maven-doxia to doxia subpackages (Resolves: #889146)

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 1.4-6
- Migrated to plexus-containers-container-default (Resolves: #878555)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-3
- Don't require post/postun jpackage-utils.

* Tue Sep 27 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-2
- Install license as doc.
- Use new package names.
- Merge and update patches.
- Use new macro

* Fri Jun 24 2011 Jaromir Capik <jcapik@redhat.com> 1.4-1
- Update to 1.4
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Dependency maven-compat introduced
- Minor spec file changes according to the latest guidelines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 11 2010 Mary Ellen Foster <mefoster at gmail.com> 1.2-4
- BuildRequire jakarta-commons-logging

* Mon May 10 2010 Mary Ellen Foster <mefoster at gmail.com> 1.2-3
- BuildRequire java >= 1:1.6.0
- Clean up changelog numbers

* Mon May 10 2010 Mary Ellen Foster <mefoster at gmail.com> 1.2-2
- Get (Build)Requirements right

* Wed Mar 31 2010 Mary Ellen Foster <mefoster at gmail.com> 1.2-1
- Initial version
- Don't run tests until maven-surefire is rebuilt

