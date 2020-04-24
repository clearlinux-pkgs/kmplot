#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmplot
Version  : 20.04.0
Release  : 18
URL      : https://download.kde.org/stable/release-service/20.04.0/src/kmplot-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/kmplot-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/kmplot-20.04.0.tar.xz.sig
Summary  : Mathematical Function Plotter
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kmplot-bin = %{version}-%{release}
Requires: kmplot-data = %{version}-%{release}
Requires: kmplot-lib = %{version}-%{release}
Requires: kmplot-license = %{version}-%{release}
Requires: kmplot-locales = %{version}-%{release}
Requires: kmplot-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kmplot package.
Group: Binaries
Requires: kmplot-data = %{version}-%{release}
Requires: kmplot-license = %{version}-%{release}

%description bin
bin components for the kmplot package.


%package data
Summary: data components for the kmplot package.
Group: Data

%description data
data components for the kmplot package.


%package doc
Summary: doc components for the kmplot package.
Group: Documentation
Requires: kmplot-man = %{version}-%{release}

%description doc
doc components for the kmplot package.


%package lib
Summary: lib components for the kmplot package.
Group: Libraries
Requires: kmplot-data = %{version}-%{release}
Requires: kmplot-license = %{version}-%{release}

%description lib
lib components for the kmplot package.


%package license
Summary: license components for the kmplot package.
Group: Default

%description license
license components for the kmplot package.


%package locales
Summary: locales components for the kmplot package.
Group: Default

%description locales
locales components for the kmplot package.


%package man
Summary: man components for the kmplot package.
Group: Default

%description man
man components for the kmplot package.


%prep
%setup -q -n kmplot-20.04.0
cd %{_builddir}/kmplot-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587690751
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587690751
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmplot
cp %{_builddir}/kmplot-20.04.0/COPYING %{buildroot}/usr/share/package-licenses/kmplot/133efad5329acf364135c569ac01ec084c3d4647
cp %{_builddir}/kmplot-20.04.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmplot/1bd373e4851a93027ba70064bd7dbdc6827147e1
pushd clr-build
%make_install
popd
%find_lang kmplot

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kmplot

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmplot.desktop
/usr/share/config.kcfg/kmplot.kcfg
/usr/share/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
/usr/share/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
/usr/share/dbus-1/interfaces/org.kde.kmplot.Parser.xml
/usr/share/dbus-1/interfaces/org.kde.kmplot.View.xml
/usr/share/icons/hicolor/128x128/apps/kmplot.png
/usr/share/icons/hicolor/16x16/apps/kmplot.png
/usr/share/icons/hicolor/22x22/apps/kmplot.png
/usr/share/icons/hicolor/32x32/apps/kmplot.png
/usr/share/icons/hicolor/48x48/apps/kmplot.png
/usr/share/icons/hicolor/64x64/apps/kmplot.png
/usr/share/icons/hicolor/scalable/apps/kmplot.svgz
/usr/share/kservices5/kmplot_part.desktop
/usr/share/kxmlgui5/kmplot/kmplot_part.rc
/usr/share/kxmlgui5/kmplot/kmplot_part_readonly.rc
/usr/share/kxmlgui5/kmplot/kmplot_shell.rc
/usr/share/metainfo/org.kde.kmplot.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmplot/commands.docbook
/usr/share/doc/HTML/ca/kmplot/configuration.docbook
/usr/share/doc/HTML/ca/kmplot/credits.docbook
/usr/share/doc/HTML/ca/kmplot/dcop.docbook
/usr/share/doc/HTML/ca/kmplot/developer.docbook
/usr/share/doc/HTML/ca/kmplot/firststeps.docbook
/usr/share/doc/HTML/ca/kmplot/index.cache.bz2
/usr/share/doc/HTML/ca/kmplot/index.docbook
/usr/share/doc/HTML/ca/kmplot/install.docbook
/usr/share/doc/HTML/ca/kmplot/introduction.docbook
/usr/share/doc/HTML/ca/kmplot/reference.docbook
/usr/share/doc/HTML/ca/kmplot/using.docbook
/usr/share/doc/HTML/de/kmplot/index.cache.bz2
/usr/share/doc/HTML/de/kmplot/index.docbook
/usr/share/doc/HTML/de/kmplot/main.png
/usr/share/doc/HTML/de/kmplot/popup.png
/usr/share/doc/HTML/de/kmplot/settings-colors.png
/usr/share/doc/HTML/de/kmplot/settings-constants.png
/usr/share/doc/HTML/de/kmplot/settings-coords.png
/usr/share/doc/HTML/de/kmplot/settings-diagram.png
/usr/share/doc/HTML/de/kmplot/settings-fonts.png
/usr/share/doc/HTML/de/kmplot/settings-general.png
/usr/share/doc/HTML/en/kmplot/edu-logo.png
/usr/share/doc/HTML/en/kmplot/index.cache.bz2
/usr/share/doc/HTML/en/kmplot/index.docbook
/usr/share/doc/HTML/en/kmplot/main.png
/usr/share/doc/HTML/en/kmplot/popup.png
/usr/share/doc/HTML/en/kmplot/settings-colors.png
/usr/share/doc/HTML/en/kmplot/settings-constants.png
/usr/share/doc/HTML/en/kmplot/settings-coords.png
/usr/share/doc/HTML/en/kmplot/settings-diagram.png
/usr/share/doc/HTML/en/kmplot/settings-fonts.png
/usr/share/doc/HTML/en/kmplot/settings-general.png
/usr/share/doc/HTML/en/kmplot/threeplots.png
/usr/share/doc/HTML/es/kmplot/commands.docbook
/usr/share/doc/HTML/es/kmplot/configuration.docbook
/usr/share/doc/HTML/es/kmplot/credits.docbook
/usr/share/doc/HTML/es/kmplot/dcop.docbook
/usr/share/doc/HTML/es/kmplot/developer.docbook
/usr/share/doc/HTML/es/kmplot/firststeps.docbook
/usr/share/doc/HTML/es/kmplot/index.cache.bz2
/usr/share/doc/HTML/es/kmplot/index.docbook
/usr/share/doc/HTML/es/kmplot/install.docbook
/usr/share/doc/HTML/es/kmplot/introduction.docbook
/usr/share/doc/HTML/es/kmplot/reference.docbook
/usr/share/doc/HTML/es/kmplot/threeplots.png
/usr/share/doc/HTML/es/kmplot/using.docbook
/usr/share/doc/HTML/et/kmplot/commands.docbook
/usr/share/doc/HTML/et/kmplot/configuration.docbook
/usr/share/doc/HTML/et/kmplot/credits.docbook
/usr/share/doc/HTML/et/kmplot/dcop.docbook
/usr/share/doc/HTML/et/kmplot/developer.docbook
/usr/share/doc/HTML/et/kmplot/firststeps.docbook
/usr/share/doc/HTML/et/kmplot/index.cache.bz2
/usr/share/doc/HTML/et/kmplot/index.docbook
/usr/share/doc/HTML/et/kmplot/install.docbook
/usr/share/doc/HTML/et/kmplot/introduction.docbook
/usr/share/doc/HTML/et/kmplot/reference.docbook
/usr/share/doc/HTML/et/kmplot/using.docbook
/usr/share/doc/HTML/fr/kmplot/commands.docbook
/usr/share/doc/HTML/fr/kmplot/configuration.docbook
/usr/share/doc/HTML/fr/kmplot/credits.docbook
/usr/share/doc/HTML/fr/kmplot/dcop.docbook
/usr/share/doc/HTML/fr/kmplot/developer.docbook
/usr/share/doc/HTML/fr/kmplot/firststeps.docbook
/usr/share/doc/HTML/fr/kmplot/index.cache.bz2
/usr/share/doc/HTML/fr/kmplot/index.docbook
/usr/share/doc/HTML/fr/kmplot/install.docbook
/usr/share/doc/HTML/fr/kmplot/introduction.docbook
/usr/share/doc/HTML/fr/kmplot/main.png
/usr/share/doc/HTML/fr/kmplot/popup.png
/usr/share/doc/HTML/fr/kmplot/reference.docbook
/usr/share/doc/HTML/fr/kmplot/settings-colors.png
/usr/share/doc/HTML/fr/kmplot/settings-constants.png
/usr/share/doc/HTML/fr/kmplot/settings-coords.png
/usr/share/doc/HTML/fr/kmplot/settings-diagram.png
/usr/share/doc/HTML/fr/kmplot/settings-fonts.png
/usr/share/doc/HTML/fr/kmplot/settings-general.png
/usr/share/doc/HTML/fr/kmplot/settings-graphing.png
/usr/share/doc/HTML/fr/kmplot/using.docbook
/usr/share/doc/HTML/gl/kmplot/commands.docbook
/usr/share/doc/HTML/gl/kmplot/configuration.docbook
/usr/share/doc/HTML/gl/kmplot/credits.docbook
/usr/share/doc/HTML/gl/kmplot/dcop.docbook
/usr/share/doc/HTML/gl/kmplot/developer.docbook
/usr/share/doc/HTML/gl/kmplot/firststeps.docbook
/usr/share/doc/HTML/gl/kmplot/index.cache.bz2
/usr/share/doc/HTML/gl/kmplot/index.docbook
/usr/share/doc/HTML/gl/kmplot/install.docbook
/usr/share/doc/HTML/gl/kmplot/introduction.docbook
/usr/share/doc/HTML/gl/kmplot/reference.docbook
/usr/share/doc/HTML/gl/kmplot/using.docbook
/usr/share/doc/HTML/it/kmplot/commands.docbook
/usr/share/doc/HTML/it/kmplot/configuration.docbook
/usr/share/doc/HTML/it/kmplot/credits.docbook
/usr/share/doc/HTML/it/kmplot/dcop.docbook
/usr/share/doc/HTML/it/kmplot/developer.docbook
/usr/share/doc/HTML/it/kmplot/firststeps.docbook
/usr/share/doc/HTML/it/kmplot/index.cache.bz2
/usr/share/doc/HTML/it/kmplot/index.docbook
/usr/share/doc/HTML/it/kmplot/install.docbook
/usr/share/doc/HTML/it/kmplot/introduction.docbook
/usr/share/doc/HTML/it/kmplot/reference.docbook
/usr/share/doc/HTML/it/kmplot/using.docbook
/usr/share/doc/HTML/nl/kmplot/commands.docbook
/usr/share/doc/HTML/nl/kmplot/configuration.docbook
/usr/share/doc/HTML/nl/kmplot/credits.docbook
/usr/share/doc/HTML/nl/kmplot/dcop.docbook
/usr/share/doc/HTML/nl/kmplot/developer.docbook
/usr/share/doc/HTML/nl/kmplot/edu-logo.png
/usr/share/doc/HTML/nl/kmplot/firststeps.docbook
/usr/share/doc/HTML/nl/kmplot/index.cache.bz2
/usr/share/doc/HTML/nl/kmplot/index.docbook
/usr/share/doc/HTML/nl/kmplot/install.docbook
/usr/share/doc/HTML/nl/kmplot/introduction.docbook
/usr/share/doc/HTML/nl/kmplot/kfkt.png
/usr/share/doc/HTML/nl/kmplot/ksys1.png
/usr/share/doc/HTML/nl/kmplot/ksys2.png
/usr/share/doc/HTML/nl/kmplot/ksys3.png
/usr/share/doc/HTML/nl/kmplot/main.png
/usr/share/doc/HTML/nl/kmplot/popup.png
/usr/share/doc/HTML/nl/kmplot/reference.docbook
/usr/share/doc/HTML/nl/kmplot/settings-colors.png
/usr/share/doc/HTML/nl/kmplot/settings-coords.png
/usr/share/doc/HTML/nl/kmplot/settings-diagram.png
/usr/share/doc/HTML/nl/kmplot/settings-fonts.png
/usr/share/doc/HTML/nl/kmplot/settings-general.png
/usr/share/doc/HTML/nl/kmplot/using.docbook
/usr/share/doc/HTML/pl/kmplot/commands.docbook
/usr/share/doc/HTML/pl/kmplot/configuration.docbook
/usr/share/doc/HTML/pl/kmplot/credits.docbook
/usr/share/doc/HTML/pl/kmplot/dcop.docbook
/usr/share/doc/HTML/pl/kmplot/developer.docbook
/usr/share/doc/HTML/pl/kmplot/firststeps.docbook
/usr/share/doc/HTML/pl/kmplot/index.cache.bz2
/usr/share/doc/HTML/pl/kmplot/index.docbook
/usr/share/doc/HTML/pl/kmplot/install.docbook
/usr/share/doc/HTML/pl/kmplot/introduction.docbook
/usr/share/doc/HTML/pl/kmplot/main.png
/usr/share/doc/HTML/pl/kmplot/popup.png
/usr/share/doc/HTML/pl/kmplot/reference.docbook
/usr/share/doc/HTML/pl/kmplot/settings-colors.png
/usr/share/doc/HTML/pl/kmplot/settings-constants.png
/usr/share/doc/HTML/pl/kmplot/settings-coords.png
/usr/share/doc/HTML/pl/kmplot/settings-diagram.png
/usr/share/doc/HTML/pl/kmplot/settings-fonts.png
/usr/share/doc/HTML/pl/kmplot/settings-general.png
/usr/share/doc/HTML/pl/kmplot/using.docbook
/usr/share/doc/HTML/pt/kmplot/commands.docbook
/usr/share/doc/HTML/pt/kmplot/configuration.docbook
/usr/share/doc/HTML/pt/kmplot/credits.docbook
/usr/share/doc/HTML/pt/kmplot/dcop.docbook
/usr/share/doc/HTML/pt/kmplot/developer.docbook
/usr/share/doc/HTML/pt/kmplot/firststeps.docbook
/usr/share/doc/HTML/pt/kmplot/index.cache.bz2
/usr/share/doc/HTML/pt/kmplot/index.docbook
/usr/share/doc/HTML/pt/kmplot/install.docbook
/usr/share/doc/HTML/pt/kmplot/introduction.docbook
/usr/share/doc/HTML/pt/kmplot/reference.docbook
/usr/share/doc/HTML/pt/kmplot/using.docbook
/usr/share/doc/HTML/pt_BR/kmplot/commands.docbook
/usr/share/doc/HTML/pt_BR/kmplot/configuration.docbook
/usr/share/doc/HTML/pt_BR/kmplot/credits.docbook
/usr/share/doc/HTML/pt_BR/kmplot/dcop.docbook
/usr/share/doc/HTML/pt_BR/kmplot/developer.docbook
/usr/share/doc/HTML/pt_BR/kmplot/edu-logo.png
/usr/share/doc/HTML/pt_BR/kmplot/firststeps.docbook
/usr/share/doc/HTML/pt_BR/kmplot/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmplot/index.docbook
/usr/share/doc/HTML/pt_BR/kmplot/install.docbook
/usr/share/doc/HTML/pt_BR/kmplot/introduction.docbook
/usr/share/doc/HTML/pt_BR/kmplot/kfkt.png
/usr/share/doc/HTML/pt_BR/kmplot/ksys1.png
/usr/share/doc/HTML/pt_BR/kmplot/ksys2.png
/usr/share/doc/HTML/pt_BR/kmplot/ksys3.png
/usr/share/doc/HTML/pt_BR/kmplot/main.png
/usr/share/doc/HTML/pt_BR/kmplot/popup.png
/usr/share/doc/HTML/pt_BR/kmplot/reference.docbook
/usr/share/doc/HTML/pt_BR/kmplot/settings-colors.png
/usr/share/doc/HTML/pt_BR/kmplot/settings-constants.png
/usr/share/doc/HTML/pt_BR/kmplot/settings-coords.png
/usr/share/doc/HTML/pt_BR/kmplot/settings-diagram.png
/usr/share/doc/HTML/pt_BR/kmplot/settings-fonts.png
/usr/share/doc/HTML/pt_BR/kmplot/settings-general.png
/usr/share/doc/HTML/pt_BR/kmplot/threeplots.png
/usr/share/doc/HTML/pt_BR/kmplot/using.docbook
/usr/share/doc/HTML/ru/kmplot/commands.docbook
/usr/share/doc/HTML/ru/kmplot/configuration.docbook
/usr/share/doc/HTML/ru/kmplot/credits.docbook
/usr/share/doc/HTML/ru/kmplot/dcop.docbook
/usr/share/doc/HTML/ru/kmplot/developer.docbook
/usr/share/doc/HTML/ru/kmplot/firststeps.docbook
/usr/share/doc/HTML/ru/kmplot/index.cache.bz2
/usr/share/doc/HTML/ru/kmplot/index.docbook
/usr/share/doc/HTML/ru/kmplot/install.docbook
/usr/share/doc/HTML/ru/kmplot/introduction.docbook
/usr/share/doc/HTML/ru/kmplot/reference.docbook
/usr/share/doc/HTML/ru/kmplot/using.docbook
/usr/share/doc/HTML/sv/kmplot/commands.docbook
/usr/share/doc/HTML/sv/kmplot/configuration.docbook
/usr/share/doc/HTML/sv/kmplot/credits.docbook
/usr/share/doc/HTML/sv/kmplot/dcop.docbook
/usr/share/doc/HTML/sv/kmplot/developer.docbook
/usr/share/doc/HTML/sv/kmplot/firststeps.docbook
/usr/share/doc/HTML/sv/kmplot/index.cache.bz2
/usr/share/doc/HTML/sv/kmplot/index.docbook
/usr/share/doc/HTML/sv/kmplot/install.docbook
/usr/share/doc/HTML/sv/kmplot/introduction.docbook
/usr/share/doc/HTML/sv/kmplot/main.png
/usr/share/doc/HTML/sv/kmplot/reference.docbook
/usr/share/doc/HTML/sv/kmplot/using.docbook
/usr/share/doc/HTML/uk/kmplot/index.cache.bz2
/usr/share/doc/HTML/uk/kmplot/index.docbook
/usr/share/doc/HTML/uk/kmplot/main.png
/usr/share/doc/HTML/uk/kmplot/popup.png
/usr/share/doc/HTML/uk/kmplot/settings-colors.png
/usr/share/doc/HTML/uk/kmplot/settings-constants.png
/usr/share/doc/HTML/uk/kmplot/settings-coords.png
/usr/share/doc/HTML/uk/kmplot/settings-diagram.png
/usr/share/doc/HTML/uk/kmplot/settings-fonts.png
/usr/share/doc/HTML/uk/kmplot/settings-general.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kmplotpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmplot/133efad5329acf364135c569ac01ec084c3d4647
/usr/share/package-licenses/kmplot/1bd373e4851a93027ba70064bd7dbdc6827147e1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kmplot.1
/usr/share/man/de/man1/kmplot.1
/usr/share/man/es/man1/kmplot.1
/usr/share/man/et/man1/kmplot.1
/usr/share/man/fr/man1/kmplot.1
/usr/share/man/gl/man1/kmplot.1
/usr/share/man/it/man1/kmplot.1
/usr/share/man/man1/kmplot.1
/usr/share/man/nl/man1/kmplot.1
/usr/share/man/pl/man1/kmplot.1
/usr/share/man/pt/man1/kmplot.1
/usr/share/man/pt_BR/man1/kmplot.1
/usr/share/man/ru/man1/kmplot.1
/usr/share/man/sv/man1/kmplot.1
/usr/share/man/uk/man1/kmplot.1

%files locales -f kmplot.lang
%defattr(-,root,root,-)

