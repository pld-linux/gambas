Summary:	Gambas - a free VB-like language
Summary(pl):	Gambas - wolnodostêpny jêzyk podobny do VB
Name:		gambas
Version:	1.0.14
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/gambas/%{name}-%{version}.tar.bz2
# Source0-md5:	b387cefe3e30c005234fd8d1e5441e75
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://gambas.sourceforge.net/
BuildRequires:	SDL_mixer-devel
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic(tm). With Gambas, you can
quickly design your program GUI, access MySQL or PostgreSQL databases,
pilot KDE applications with DCOP, translate your program into many
languages, and so on...

This package provides the command-line utilities, as well as the
Gambas interpreter needed to run Gambas applications.

%description -l pl
Gambas to wolnodostêpne ¶rodowisko programistyczne oparte na
interpreterze Basica z rozszerzeniami obiektowymi, podobnym do Visual
Basica(TM). Przy pomocy Gambasa mo¿na szybko projektowaæ graficzne
interfejsy u¿ytkownika, odwo³ywaæ siê do baz danych MySQL i
PostgreSQL, sterowaæ aplikacjami KDE poprzez DCOP, t³umaczyæ program
na wiele jêzyków itd.

Ten pakiet dostarcza narzêdzia dzia³aj±ce z linii poleceñ, a tak¿e
interpreter potrzebny do uruchamiania aplikacji Gambas.

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

%package ide
Summary:	The Gambas IDE
Summary(pl):	IDE dla Gambas
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-debug = %{version}-%{release}
Requires:	%{name}-gb-qt = %{version}-%{release}
Requires:	%{name}-gb-qt-editor = %{version}-%{release}
Requires:	%{name}-gb-qt-ext = %{version}-%{release}

%description ide
This package includes the complete Gambas Development Environment,
with the database manager and all necessary components.

%description ide -l pl
Ten pakiet zawiera kompletne ¶rodowisko programistyczne, ³±cznie
z mened¿erem baz danych i wszystkimi niezbêdnymi komponentami.

%package examples
Summary:	The examples for Gambas language
Summary(pl):	Przyk³ady dla jêzyka Gambas
Group:		Development/Languages
Requires:	%{name}-ide = %{version}-%{release}

%description examples
The gambas-examples package contains some examples for Gambas.

%description examples -l pl
Ten pakiet zawiera kilka przyk³adów dla Gambas.

%package gb-compress
Summary:	The Gambas compression component
Summary(pl):	Gambas - komponent do kompresji
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-compress
This component allows you to compress/uncompress data or files with
the bzip2 and zip algorithms.

%description gb-compress -l pl
Ten komponent pozwala pakowaæ/rozpakowywaæ dane lub pliki przy u¿yciu
algorytmów bzip2 i zip.

%package gb-db
Summary:	The Gambas database component
Summary(pl):	Gambas - komponent bazodanowy
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-db
This component allows you to access many databases management systems,
provided that you install the needed driver packages.

%description gb-db -l pl
Ten komponent pozwala na dostêp do wielu systemów bazodanowych pod
warunkiem doinstalowania wymaganych pakietów sterowników.

%package gb-db-mysql
Summary:	The MySQL driver for the Gambas database component
Summary(pl):	Gambas - sterownik do MySQL dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-mysql
This component allows you to access MySQL databases.

%description gb-db-mysql -l pl
Ten komponent pozwala na dostêp do bazy danych MySQL.

%package gb-db-postgresql
Summary:	The PostgreSQL driver for the Gambas database component
Summary(pl):	Gambas - sterownik do PostgreSQL dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-postgresql
This component allows you to access PostgreSQL databases.

%description gb-db-postgresql -l pl
Ten komponent pozwala na dostêp do bazy danych PostgreSQL.

%package gb-db-sqlite
Summary:	The SQLite driver for the Gambas database component
Summary(pl):	Gambas - sterownik do SQLite dla komponentu bazodanowego
Group:		Development/Languages
Requires:	%{name}-gb-db = %{version}-%{release}

%description gb-db-sqlite
This component allows you to access SQLite databases.

%description gb-db-sqlite -l pl
Ten komponent pozwala na dostêp do bazy danych SQLite.

%package gb-debug
Summary:	The debugger helper component for the Gambas IDE
Summary(pl):	Gambas - komponent debuggera dla IDE
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-debug
This component helps the IDE to debug Gambas programs.

%description gb-debug -l pl
Komponent przeznaczony dla IDE Gambasa, przydatny przy odpluskwianiu
programów.

%package gb-eval
Summary:	The Gambas expression evaluator component
Summary(pl):	Gambas - komponent do obliczania wyra¿eñ
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-eval
This component allows you to evaluate expressions at runtime. It is
used by the Gambas Eval() function.

%description gb-eval -l pl
Ten komponent pozwala na obliczanie wyra¿eñ w programach. Jest u¿ywany
przez funkcjê Gambasa Eval().

%package gb-net
Summary:	The Gambas networking component
Summary(pl):	Komponent sieciowy Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-net
This component allows you to use TCP/IP and UDP sockets, and to access
any serial ports.

%description gb-net -l pl
Ten komponent pozwala na u¿ywanie gniazd TCP/IP i UDP oraz na dostêp
do portów szeregowych.

%package gb-net-curl
Summary:	The Gambas advanced networking component
Summary(pl):	Zaawansowany komponent sieciowy Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-net = %{version}-%{release}

%description gb-net-curl
This component allows your programs to easily become FTP or HTTP
clients.

%description gb-net-curl -l pl
Ten komponent pozwala programom w ³atwy sposób staæ siê klientami FTP
lub HTTP.

%package gb-qt
Summary:	The Gambas Qt GUI component
Summary(pl):	Komponent graficznego interfejsu u¿ytkownika Qt dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-qt
This package includes the Gambas Qt GUI component.

%description gb-qt -l pl
Ten pakiet zawiera komponent graficznego interfejsu u¿ytkownika Qt dla
Gambasa.

%package gb-qt-ext
Summary:	The Gambas extended Qt GUI component
Summary(pl):	Komponent rozszerzonego graficznego interfejsu Qt dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-ext
This component includes some uncommon Qt controls.

%description gb-qt-ext -l pl
Ten komponent zawiera niektóre ma³o popularne kontrolki Qt.

%package gb-qt-editor
Summary:	The Gambas source code editor component
Summary(pl):	Komponent edytora kodu ¼ród³owego Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-editor
This component includes a Gambas source code editor with syntax
highlighting. It is used by the IDE.

%description gb-qt-editor -l pl
Ten komponent zawiera edytor kodu ¼ród³owego Gambasa z pod¶wietlaniem
sk³adni. Jest u¿ywany przez IDE.

%package gb-qt-kde
Summary:	The Gambas KDE component
Summary(pl):	Komponent KDE dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt = %{version}-%{release}

%description gb-qt-kde
This component transforms your Qt application in a KDE application,
and allows you to pilot any other KDE application with the DCOP
protocol.

%description gb-qt-kde -l pl
Ten komponent zamienia aplikacjê Qt w aplikacjê KDE i pozwala na
sterowanie dowolnymi aplikacjami KDE poprzez protokó³ DCOP.

%package gb-qt-kde-html
Summary:	The Gambas KHTML component
Summary(pl):	Komponent KHTML dla Gambasa
Group:		Development/Languages
Requires:	%{name}-gb-qt-kde = %{version}-%{release}

%description gb-qt-kde-html
This component allows you to use the KHTML Web Browser widget included
in KDE.

%description gb-qt-kde-html -l pl
Ten komponent pozwala na u¿ywanie widgetu przegl±darki WWW KHTML
zawartego w KDE.

%package gb-sdl
Summary:	The Gambas SDL component
Summary(pl):	Komponent SDL dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-sdl
This component uses only the sound part of the SDL library. It allows
you to simultaneously play many sounds and a music stored in a file.

%description gb-sdl -l pl
Ten komponent u¿ywa tylko czê¶ci d¼wiêkowej biblioteki SDL. Pozwala na
jednoczesne odtwarzanie wielu d¼wiêków i muzyki zapisanej w pliku.

%package gb-vb
Summary:	The Gambas Visual Basic(TM) compatibility component
Summary(pl):	Komponent zgodno¶ci z Visual Basicem(TM) dla Gambasa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-vb
This component aims at including some functions that imitate the
behaviour of Visual Basic(TM) functions. Use it only if you try to
port some VB projects.

%description gb-vb -l pl
Ten komponent zawiera trochê funkcji, których celem jest imitowanie
zachowania funkcji Visual Basica(TM). Nale¿y go u¿ywaæ wy³±cznie przy
próbach sportowania projektów VB.

%package gb-xml
Summary:	The Gambas XML components based on the libxml and libxslt libraries
Summary(pl):	Komponenty XML Gambasa oparte na bibliotekach libxml i libxslt
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description gb-xml
These components brings the power of the libxml and libxslt libraries
to Gambas.

%description gb-xml -l pl
Te komponenty dostarczaj± do Gambasa potêgê bibliotek libxml i
libxslt.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install app/gambas/img/logo/gambas-48x48.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gbc
%attr(755,root,root) %{_bindir}/gbi
%attr(755,root,root) %{_bindir}/gbx
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/info
%{_libdir}/%{name}/lib.gb.component
%{_datadir}/%{name}/info/gb.info
%{_datadir}/%{name}/info/gb.list

%files doc
%defattr(644,root,root,755)
%{_datadir}/%{name}/help

%files ide
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gambas
%attr(755,root,root) %{_bindir}/gambas-database-manager
%attr(755,root,root) %{_bindir}/gba
%{_desktopdir}/gambas.desktop
%{_pixmapsdir}/gambas.png

%files examples
%defattr(644,root,root,755)
%{_datadir}/%{name}/examples

%files gb-compress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.compress.*
%{_datadir}/%{name}/info/gb.compress.*

%files gb-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.so*
%{_libdir}/%{name}/lib.gb.db.component
%{_datadir}/%{name}/info/gb.db.info
%{_datadir}/%{name}/info/gb.db.list

%files gb-db-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.mysql.*

%files gb-db-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.postgresql.*

%files gb-db-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.db.sqlite.*

%files gb-debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.debug.*
%{_datadir}/%{name}/info/gb.debug.*

%files gb-eval
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.eval.*
%{_datadir}/%{name}/info/gb.eval.*

%files gb-net
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.net.so*
%{_libdir}/%{name}/lib.gb.net.component
%{_datadir}/%{name}/info/gb.net.info
%{_datadir}/%{name}/info/gb.net.list

%files gb-net-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.net.curl.so*
%{_libdir}/%{name}/lib.gb.net.curl.component
%{_datadir}/%{name}/info/gb.net.curl.info
%{_datadir}/%{name}/info/gb.net.curl.list

%files gb-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.so*
%{_libdir}/%{name}/lib.gb.qt.component
%{_datadir}/%{name}/info/gb.qt.info
%{_datadir}/%{name}/info/gb.qt.list

%files gb-qt-ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.ext.so*
%{_libdir}/%{name}/lib.gb.qt.ext.component
%{_datadir}/%{name}/info/gb.qt.ext.info
%{_datadir}/%{name}/info/gb.qt.ext.list

%files gb-qt-editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.editor.so*
%{_libdir}/%{name}/lib.gb.qt.editor.component
%{_datadir}/%{name}/info/gb.qt.editor.info
%{_datadir}/%{name}/info/gb.qt.editor.list

%files gb-qt-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.kde.so*
%{_libdir}/%{name}/lib.gb.qt.kde.component
%{_datadir}/%{name}/info/gb.qt.kde.info
%{_datadir}/%{name}/info/gb.qt.kde.list

%files gb-qt-kde-html
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.qt.kde.html.so*
%{_libdir}/%{name}/lib.gb.qt.kde.html.component
%{_datadir}/%{name}/info/gb.qt.kde.html.info
%{_datadir}/%{name}/info/gb.qt.kde.html.list

%files gb-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.sdl.so*
%{_libdir}/%{name}/lib.gb.sdl.component
%{_datadir}/%{name}/info/gb.sdl.info
%{_datadir}/%{name}/info/gb.sdl.list

%files gb-vb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.vb.so*
%{_libdir}/%{name}/lib.gb.vb.component
%{_datadir}/%{name}/info/gb.vb.info
%{_datadir}/%{name}/info/gb.vb.list

%files gb-xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/lib.gb.xml.libxml.*
%{_datadir}/%{name}/info/gb.xml.libxml.*
