Summary:	Gambas - a free VB-like language
Summary(pl):	Gambas - wolnodostêpny jêzyk VB-podobny
Name:		gambas
License:	GPL
Group:		Development/Languages
Version:	0.90
Release:	0.1	
Source0:	http://gambas.sourceforge.net/%{name}-%{version}.tar.bz2
# Source0-md5:	1f3211e2c97a354205123a71441e6ced
URL:		http://gambas.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm). With Gambas, you can
quickly design your program GUI, access MySQL or PostgreSQL databases,
pilot KDE applications with DCOP, translate your program into many
languages, and so on...

This package only provides the command-line utilities. You will need
gambas-lib for the required components and gambas-gui for the actual
VB-like environment.

%description -l pl
Gambas to wolnodostêpne ¶rodowisko programistyczne oparte na
interpreterze Basica z rozszerzeniami obiektowymi, podobnym do Visual
Basica(TM). Przy pomocy Gambasa mo¿na szybko projektowaæ graficzne
interfejsy u¿ytkownika, odwo³ywaæ siê do baz danych MySQL i
PostgreSQL, sterowaæ aplikacjami KDE poprzez DCOP, t³umaczyæ program
na wiele jêzyków itd.

Ten pakiet dostarcza tylko narzêdzia dzia³aj±ce z linii poleceñ. Do
¶rodowiska programistycznego potrzebne s± jeszcze gambas-lib z
komponentami oraz gambas-gui z samym ¶rodowiskiem podobnym do VB.

%package doc
Summary:	Documentation for Gambas language
Summary(pl):	Dokumentacja dla jêzyka Gambas
Group:		Development/Languages

%description doc
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm). With Gambas, you can
quickly design your program GUI, access MySQL or PostgreSQL databases,
pilot KDE applications with DCOP, translate your program into many
languages, and so on...

This package contains Gambas language documentation.

%description doc -l pl
Gambas to wolnodostêpne ¶rodowisko programistyczne oparte na
interpreterze Basica z rozszerzeniami obiektowymi, podobnym do Visual
Basica(TM). Przy pomocy Gambasa mo¿na szybko projektowaæ graficzne
interfejsy u¿ytkownika, odwo³ywaæ siê do baz danych MySQL i
PostgreSQL, sterowaæ aplikacjami KDE poprzez DCOP, t³umaczyæ program
na wiele jêzyków itd.

Ten pakiet zawiera dokumentacjê dla jêzyka Gambas.

%package libs
Summary:	Gambas language components and libraries
Summary(pl):	Komponenty i biblioteki jêzyka Gambas
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description libs
This package provides the components for Gambas language. You will
need the gambas package for the compiler/interpreter and gambas-gui
for the actual VB-like environment.

%description libs -l pl
Ten pakiet dostarcza komponenty dla jêzyka Gambas. Oprócz niego do
pe³nego ¶rodowiska potrzebny jest pakiet gambas z
kompilatorem/interpreterem oraz gambas-gui z w³a¶ciwym graficznym
interfejsem.

%package devel
Summary:	Header file for Gambas component development
Summary(pl):	Plik nag³ówkowy do tworzenia komponentów jêzyka Gambas
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes the header file necessary for writing your own
Gambas components, as well as the source for the Gambas GUI components
necessary for building the gambas-gui package.

%description devel -l pl
Ten pakiet zawiera plik nag³ówkowy potrzebny do pisania w³asnych
komponentów Gambasa, a tak¿e ¼ród³a komponentów GUI Gambasa potrzebne
do budowania pakietu gambas-gui.

%prep
%setup -q

%build
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
# workaround for broken libtool
rm -rf $RPM_BUILD_ROOT
export SED=sed
export PATH=${RPM_BUILD_ROOT}%{_bindir}:$PWD/src/comp:$PATH
#make DESTDIR=${RPM_BUILD_ROOT} install
#install -d ${RPM_BUILD_ROOT}%{_bindir}/
#install -d ${RPM_BUILD_ROOT}%{_datadir}/doc/%{name}-%{version}
#install -d ${RPM_BUILD_ROOT}%{_includedir}/
#install -d ${RPM_BUILD_ROOT}%{_includedir}/%{name}
#install -d ${RPM_BUILD_ROOT}%appdir/
#install -d ${RPM_BUILD_ROOT}%appdir/lib/
#install -s -m 0755 src/exec/gbx ${RPM_BUILD_ROOT}%{_bindir}/
#install -s -m 0755 src/comp/gba ${RPM_BUILD_ROOT}%{_bindir}/
#install -s -m 0755 src/comp/gbi ${RPM_BUILD_ROOT}%{_bindir}/
#install -s -m 0755 src/comp/gbc ${RPM_BUILD_ROOT}%{_bindir}/
#find src -name *.la -exec cp {} ${RPM_BUILD_ROOT}%appdir/lib \;
#find src -name *.so* -exec cp -a {} ${RPM_BUILD_ROOT}%appdir/lib \;
#cp -a src/share/gambas.h ${RPM_BUILD_ROOT}%{_includedir}/%{name}
#cp -av examples ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}
##cp -av help ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}
#find ${RPM_BUILD_ROOT} -size 0 -exec rm -f {} \;
#tar cjvf ${RPM_BUILD_ROOT}%appdir/gambas-gui-%{version}.tar.bz2 app/ `find src/ -name *.component`
#
%clean
rm -rf $RPM_BUILD_ROOT

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README
#%appdir/lib/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README
#%appdir/lib/*.so
#%appdir/lib/*.la
#%{_includedir}/%{name}
#%appdir/gambas-gui-%{version}.tar.bz2

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

#%post -n gambas-doc
#ln -s /usr/share/doc/%{name}-doc-%{version}/examples %{appdir}/
#mkdir -p %{appdir}/share
#ln -s /usr/share/doc/%{name}-doc-%{version}/help %{appdir}/share/help

#%postun -n gambas-doc
#rm -f %{appdir}/examples
#rm -f %{appdir}/share/help
#rmdir %{appdir}/share

#%post -n gambas
#mkdir -p %appdir/bin/
#mv -f /usr/bin/gbx %appdir/bin/gbx-real
#ln -s %appdir/bin/gbx-real /usr/bin/gbx
