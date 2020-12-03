%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?fedora} > 12 || 0%{?rhel} && 0%{?dist_raw} >= 75
%bcond_without python3
%else
%bcond_with python3
%endif

# centos 7.2 and lower versions don't have %py2_* macros, so define it manually
%if 0%{?rhel} && 0%{?dist_raw} <= 72
%{!?py2_build: %global py2_build %py_build}
%{!?py2_install: %global py2_install %py_install}
%endif

%define pkgname pytest
%global sum Samll tests framework
%global descr The pytest framework makes it easy to write small tests, yet scales to support complex functional testing 

Name: python-%{pkgname}
Summary: %{sum}
Version: 4.6.11
Release: CROC1%{?dist}
License: Apache License, Version 2.0

Group: Development/Testing
URL: https://github.com/patrys/httmock
Source0: %{pkgname}-%{version}.tar.gz


BuildArch: noarch

%description
%{descr}


%package -n python2-%{pkgname}
Summary:       %{sum}
Requires:      python-requests >= 1.0.0
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-requests >= 1.0.0
Obsoletes:     python-httmock < 1.2.3-3%{?dist}

%description -n python2-%{pkgname}
%{descr}


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:       %{sum}
Requires:      python36-requests >= 1.0.0
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python36-requests >= 1.0.0


%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}
%endif


%prep
%setup -q -n %{pkgname}-%{version}


%build
%py2_build

%if %{with python3}
%py3_build
%endif


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%py2_install

%if %{with python3}
%py3_install
%endif


%clean
rm -rf %{buildroot}


%files -n python2-%{pkgname}
%defattr(-,root,root,-)
%{python2_sitelib}/*

%doc README.rst LICENSE

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%{python3_sitelib}/*

%doc README.rst LICENSE
%endif

%changelog
* Thu Dec 03 2020 Andrey Kulaev <adkulaev@gmail.com> 4.6.11-1
- Initial build.
