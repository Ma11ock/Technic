%global srcname technic

Name: technic
Version: 4.0.0
Release: 0%{?dist}
License: GPLv3
Summary: A custom minecraft launcher that automatically downloads and updates modpacks
Url: https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://github.com/Ma11ock/Technic
# cd Technic
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
ExclusiveArch: %{java_arches} noarch

BuildRequires: maven-local
BuildRequires: java-17

Requires: java-17
Requires: java-11
Requires: java-1.8.0
Requires: java

%description
Technic is a launcher for minecraft that provides a way to easily
install and update mods.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
%mvn_build

%install
%mvn_install


#-- FILES ---------------------------------------------------------------------#
%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md
%license LICENSE
#%files javadoc -f .mfiles-javadoc

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Wed Jan 4 2023 Ryan Jeffrey <ryan@ryanmj.xyz> 4.0.0-1
- Initial packaging
