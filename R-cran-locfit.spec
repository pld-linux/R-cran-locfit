%define		fversion	%(echo %{version} |tr r -)
%define		modulename	locfit
Summary:	Local regression, likelihood and density estimation
Name:		R-cran-%{modulename}
Version:	1.5r9.1
Release:	1
License:	GPLv2
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	38af7791c9cda78e2804020e65ac7fb4
BuildRequires:	R >= 2.8.1
BuildRequires:	texlive-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Local regression, likelihood and density estimation.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{modulename}/DESCRIPTION
%doc %{_libdir}/R/library/%{modulename}/html
%doc %{_libdir}/R/library/%{modulename}/NEWS
%dir %{_libdir}/R/library/%{modulename}
%{_libdir}/R/library/%{modulename}/INDEX
%{_libdir}/R/library/%{modulename}/NAMESPACE
%{_libdir}/R/library/%{modulename}/Meta
%{_libdir}/R/library/%{modulename}/R
%{_libdir}/R/library/%{modulename}/help
%{_libdir}/R/library/%{modulename}/data
%dir %{_libdir}/R/library/%{modulename}/libs
%attr(755,root,root) %{_libdir}/R/library/%{modulename}/libs/locfit.so
