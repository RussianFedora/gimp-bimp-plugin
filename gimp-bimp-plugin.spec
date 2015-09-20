Name:           gimp-bimp-plugin
Version:        1.16
Release:        1%{?dist}
Summary:        Batch Image Manipulation Plugin

License:        GPLv2+
URL:            http://www.alessandrofrancesconi.it/projects/bimp/
Source0:        https://github.com/alessandrofrancesconi/gimp-plugin-bimp/archive/v%{version}.tar.gz

BuildRequires:  pcre-devel
BuildRequires:  gimp-devel >= 2.6.0
Requires:       gimp >= 2.6.0
 
%description
Use BIMP to apply a set of GIMP manipulations to groups of images.

%prep
%autosetup -n gimp-plugin-bimp-%{version}
sed -i -e 's|gcc -o ./bin/bimp|gcc -o ./bin/bimp $(CFLAGS)|' Makefile
echo '#!/bin/bash' > configure
chmod +x configure

%build
%configure
make %{?_smp_mflags}

%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
install -m 0755 -p ./bin/bimp %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
mkdir -p %{buildroot}%{_datadir}/locale/
cp -ai ./bimp-locale/* %{buildroot}%{_datadir}/locale/
find %{buildroot}%{_datadir}/locale/ -name "*.po" -exec rm -rf {} \;
%find_lang gimp20-plugin-bimp

%files -f gimp20-plugin-bimp.lang
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/gimp/2.0/plug-ins/bimp

%changelog
* Sun Sep 20 2015 Maxim Orlov <murmansksity@gmail.com> - 1.16-1
- Update to 1.16

* Mon Jul 13 2015 Maxim Orlov <murmansksity@gmail.com> - 1.15-1
- Update to 1.15

* Sat Jul 11 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 1.14-1
- Clean spec

* Fri Jul 10 2015 Maxim Orlov <murmansksity@gmail.com> - 1.14-1
- Initial package.
