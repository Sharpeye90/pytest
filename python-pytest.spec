%bcond_without python3

%define pkgname pytest
%global pylib_version 1.4.8

Name:           python-%{pkgname}
Version:        3.0.7
Release:        CROC4%{?dist}
Summary:        Simple powerful testing with Python
License:        MIT
URL:            http://pytest.org
Source0:        %{pkgname}-%{version}.tar.gz

BuildArch:      noarch

%description
py.test provides simple, yet powerful testing for Python.


%package -n python2-%{pkgname}
Summary:        Simple powerful testing with Python
BuildRequires:  python2-devel
BuildRequires:  python-py >= %{pylib_version}
BuildRequires:  python2-setuptools
BuildRequires:  python2-six

Requires:       python-py >= %{pylib_version}
Requires:       python2-setuptools
Requires:       python2-six

Obsoletes: 	pytest

%description -n python2-%{pkgname}
py.test provides simple, yet powerful testing for Python.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        Simple powerful testing with Python
BuildRequires:  python%{python3_pkgversion}-devel

BuildRequires:  python36-py >= %{pylib_version}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python36-six

Requires:       python36-py >= %{pylib_version}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python36-six

%description -n python%{python3_pkgversion}-%{pkgname}
py.test provides simple, yet powerful testing for Python.
%endif

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python2_version}
ln -snf pytest-%{python2_version} %{buildroot}%{_bindir}/pytest-2
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python2_version}
ln -snf py.test-%{python2_version} %{buildroot}%{_bindir}/py.test-2
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3
%endif

# use 2.X per default
ln -snf pytest-%{python2_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python2_version} %{buildroot}%{_bindir}/py.test

# remove shebangs from all scripts
find %{buildroot}%{python2_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;

%if 0%{?with_python3}
find %{buildroot}%{python3_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;
%endif

%files -n python2-%{pkgname}
%license LICENSE
%{_bindir}/pytest
%{_bindir}/pytest-2
%{_bindir}/pytest-%{python2_version}
%{_bindir}/py.test
%{_bindir}/py.test-2
%{_bindir}/py.test-%{python2_version}
%{python2_sitelib}/pytest-*.egg-info/
%{python2_sitelib}/_pytest/
%{python2_sitelib}/pytest.py*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%{_bindir}/pytest-3
%{_bindir}/pytest-%{python3_version}
%{_bindir}/py.test-3
%{_bindir}/py.test-%{python3_version}
%{python3_sitelib}/pytest-*.egg-info/
%{python3_sitelib}/_pytest/
%{python3_sitelib}/pytest.py
%{python3_sitelib}/__pycache__/pytest.*
%endif

%changelog
* Mon Dec 28 2020 Andrey Kulaev <adkulaev@gmail.com> 3.0.7-4
- Make pytest obsolete

* Wed Dec 23 2020 Andrey Kulaev <adkulaev@gmail.com> 3.0.7-3
- Actualize to fedora spec version

* Tue Dec 08 2020 Andrey Kulaev <adkulaev@gmail.com> 3.0.7-2
- Add python-py dependency 

* Thu Dec 03 2020 Andrey Kulaev <adkulaev@gmail.com> 3.0.7-1
- Initial build.
