# Created by pyp2rpm-3.3.5
%global pypi_name superlance

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        superlance plugins for supervisord

License:        BSD-derived (http://www.repoze.org/LICENSE.txt)
URL:            https://github.com/Supervisor/superlance
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(supervisor)
BuildRequires:  python3dist(supervisor)
BuildRequires:  python3dist(sphinx)

%description
superlance README Superlance is a package of plugin utilities for monitoring
and controlling processes that run under supervisor <>_.Please see
docs/index.rst for complete documentation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(supervisor)
%description -n python3-%{pypi_name}
superlance README Superlance is a package of plugin utilities for monitoring
and controlling processes that run under supervisor <>_.Please see
docs/index.rst for complete documentation.

%package -n python-%{pypi_name}-doc
Summary:        superlance documentation
%description -n python-%{pypi_name}-doc
Documentation for superlance

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
/usr/bin/crashmail
/usr/bin/crashmailbatch
/usr/bin/crashsms
/usr/bin/fatalmailbatch
/usr/bin/httpok
/usr/bin/memmon



%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Mon Jan 04 2021 Terry Patterson <terryp@wegrok.net> - 1.0.0-2
- Improve descriptions.
* Mon Jan 04 2021 Terry Patterson <terryp@wegrok.net> - 1.0.0-1
- Initial package.
