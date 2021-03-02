#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define	module moksha.common
Summary:	Common components for Moksha
Name:		python-moksha-common
Version:	1.2.4
Release:	2
License:	ASL 2.0 or MIT
Group:		Development/Libraries
Source0:	http://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	47fdd87d256eebbd1e3c62e1adea46c0
URL:		http://pypi.python.org/pypi/moksha.common
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-decorator
BuildRequires:	python-kitchen
BuildRequires:	python-mock
BuildRequires:	python-modules
BuildRequires:	python-nose
BuildRequires:	python-pytz
BuildRequires:	python-setuptools
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-decorator
BuildRequires:	python3-devel
BuildRequires:	python3-kitchen
BuildRequires:	python3-mock
BuildRequires:	python3-nose
BuildRequires:	python3-pytz
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
%endif
Requires:	python-decorator
Requires:	python-kitchen
Requires:	python-pytz
Requires:	python-six
BuildArch:	noarch
# Its a whole different package now
Conflicts:	moksha < 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common components for Moksha.

%package -n python3-moksha-common
Summary:	Common components for Moksha
Group:		Development/Libraries
Requires:	python3-decorator
Requires:	python3-kitchen
Requires:	python3-pytz
Requires:	python3-six

%description -n python3-moksha-common
Common components for Moksha.

%prep
%setup -q -n %{module}-%{version}

rm -rv *.egg*

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/moksha/common/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/moksha/common/testtools

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/moksha/common/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/moksha/common/testtools
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README COPYING AUTHORS
%attr(755,root,root) %{_bindir}/moksha
%dir %{py_sitescriptdir}/moksha
%{py_sitescriptdir}/moksha/common
%{py_sitescriptdir}/moksha.common-%{version}-py*.egg-info
%{py_sitescriptdir}/moksha.common-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-moksha-common
%defattr(644,root,root,755)
%doc README COPYING AUTHORS
%dir %{py3_sitescriptdir}/moksha
%dir %{py3_sitescriptdir}/moksha/common
%{py3_sitescriptdir}/moksha.common-%{version}-py*.egg-info
%endif
