Name:           gimp-bimp-plugin
Version:        1.14
Release:        1%{?dist}
Summary:        Batch Image Manipulation Plugin

License:        GPL-2.0+
URL:            http://www.alessandrofrancesconi.it/projects/bimp/
Source0:        https://github.com/alessandrofrancesconi/gimp-plugin-bimp/archive/v%{version}.tar.gz

BuildRequires:  pcre-devel
BuildRequires:  gimp-devel >= 2.6.0
Requires:       gimp >= 2.6.0

%description
Use BIMP to apply a set of GIMP manipulations to groups of images.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins
cp ./bin/bimp %{buildroot}%{_libdir}/gimp/2.0/plug-ins
cp -Rf ./bin/win32/bimp-locale/ %{buildroot}%{_libdir}/gimp/2.0/plug-ins

%files
%doc CHANGELOG LICENSE README.md
%defattr(-,root,root)
%dir %{_libdir}/gimp/2.0/plug-ins
%attr(0755,root,root) %{_libdir}/gimp/2.0/plug-ins/bimp
%{_libdir}/gimp/2.0/plug-ins/bimp-locale

%changelog
* Fri Jul 10 2015 Maxim Orlov <murmansksity@gmail.com> - 1.14-1
- Initial package.
