%define 	fname	SQLAlchemyManager
Summary:	Provides a sensible way of using SQLAlchemy in WSGI applications
Summary(pl.UTF-8):	Ułatwia praktyczne wykorzystanie SQLAlchemy w aplikacjach WSGI
Name:		python-%{fname}
Version:	0.1.0
Release:	0.9
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/SQLAlchemyManager/%{fname}-%{version}.tar.gz
# Source0-md5:	068b29d8e4ef97839d96a4945df4fcf9
URL:		http://pypi.python.org/pypi/SQLAlchemyManager
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This middleware sets up the standard SQLAlchemy objects in a piece of
WSGI middleware without doing anything particularly clever and without
using any global objects.

%prep
%setup -q -n %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/sqlalchemymanager
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
