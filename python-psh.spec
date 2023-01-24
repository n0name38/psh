%{!?__python3: %global __python3 /usr/bin/python3}

%bcond_without check

%global project_name psh
%global project_description %{expand:
psh allows you to spawn processes in Unix shell-style way.

Unix shell is very convenient for spawning processes, connecting them into
pipes, etc., but it has a very limited language which is often not suitable
for writing complex programs. Python is a very flexible and reach language
which is used in a wide variety of application domains, but its standard
subprocess module is very limited. psh combines the power of Python language
and an elegant shell-style way to execute processes.}

Name:    python-%project_name
Version: 0.2.12
Release: 2.CROC1%{?dist}
Summary: Process management library

Group:   Development/Languages
License: MIT
URL:     https://konishchevdmitry.github.io/%project_name/
Source:  http://pypi.python.org/packages/source/p/%project_name/%project_name-%version.tar.gz

BuildArch:     noarch
BuildRequires: make

%description %{project_description}


%package -n python%{python3_pkgversion}-%project_name
Summary: %{summary}
Requires: python%{python3_pkgversion}-pcore
Requires: python%{python3_pkgversion}-psys >= 0.3
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%if 0%{with check}
BuildRequires: python%{python3_pkgversion}-pcore
BuildRequires: python%{python3_pkgversion}-psys >= 0.3
BuildRequires: python%{python3_pkgversion}-pytest >= 2.2.4
%endif

%description -n python%{python3_pkgversion}-%project_name %{project_description}

%prep
%setup -n %project_name-%version -q


%build
%py3_build

%check
%{__python3} setup.py test

%install
%py3_install

%files -n python%{python3_pkgversion}-%project_name
%defattr(-,root,root,-)
%{python3_sitelib}/psh
%{python3_sitelib}/psh-*.egg-info
%doc ChangeLog INSTALL README.rst

%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"


%changelog
* Tue Jan 23 2023 Andrey Kulaev <adkulaev@gmail.com> - 0.2.12-2
- Add centos 8.4 support

* Wed Aug 17 2022 Dmitry Konishchev <konishchev@gmail.com> - 0.2.12-1
- New version

* Fri Apr 15 2022 Dmitry Konishchev <konishchev@gmail.com> - 0.2.11-1
- Add missing O_TRUNC to file creation mode

* Wed Jul 28 2021 Dmitry Konishchev <konishchev@gmail.com> - 0.2.10-1
- Change documentation URL

* Sun Feb 10 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.2.8-2
- Add python3 package build for EPEL

* Fri Sep 07 2018 Dmitry Konishchev <konishchev@gmail.com> - 0.2.8-1
- New version.

* Thu Sep 24 2015 Dmitry Konishchev <konishchev@gmail.com> - 0.2.5-1
- New version.

* Mon Nov 18 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.2.4-1
- New version.

* Fri Jun 28 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.2.3-2
- Don't remove *.egg-info to make setup.py with entry_points work

* Fri Dec 21 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.2.3-1
- New version.

* Thu Oct 25 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.2.2-1
- New version.

* Tue Oct 23 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.2.1-1
- New version.

* Mon Oct 22 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.2-1
- New version.

* Fri Oct 12 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.1-1
- New package.
