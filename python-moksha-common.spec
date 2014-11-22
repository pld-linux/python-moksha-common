#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define	module moksha.common
Summary:	Common components for Moksha
Name:		python-moksha-common
Version:	1.2.3
Release:	1
License:	ASL 2.0 or MIT
Group:		Development/Libraries
Source0:	http://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c0898257d033d41f8f8c7e8fdb77058d
URL:		http://pypi.python.org/pypi/moksha.common
BuildRequires:	rpm-pythonprov
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
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README COPYING AUTHORS
%attr(755,root,root) %{_bindir}/moksha
#%{py_sitescriptdir}/moksha/
%{py_sitescriptdir}/%{module}-%{version}*
%endif

%if %{with python3}
%files -n python3-moksha-common
%defattr(644,root,root,755)
%doc README COPYING AUTHORS
%{py3_sitescriptdir}/moksha/
%{py3_sitescriptdir}/%{module}-%{version}*
%{__python}3-moksha
%endif
