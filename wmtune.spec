Summary:	Window Maker Dockable Applet for Sound Cards with FM Radio
Summary(pl):	Dokowalny aplet dla Window Makera'a do kart muzycznych z radiem
Name:		wmtune
Version:	1.0
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop 
Patch0:		%{name}-SB16_FM.patch
Patch1:		%{name}-opts.patch
URL:            http://windowmaker.mezaway.org/dockapps/wmtune.html
BuildRequires: 	XFree86-devel
BuildRequires:	xpm-devel
ExclusiveArch:  %{ix86}
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
This program allows user to hear radio stations and to set an alarm
if his soundcard support this. I've patched the original source to get
scannig and tunning up and down on my Vibra16FM soundcard. After
installation you must edit your /etc/wmtunerc file (or copy 
it to ~./home/.wmtunerc and edit there) to set up proper I/O radio on 
your card address and to set up the stations. Enjoy it !

%description -l pl
Program ten umo¿liwia u¿ywanie radia na karcie d¼wiêkowej oraz ustawianie
alarmu, je¿eli karta to umo¿liwia. Zmieni³em nieco oryginalne ¼ród³a aby
uzyskaæ przestrajanie i wyszukiwanie stacji na mojej karcie Vibra16FM.
Po instalacji nale¿y wyedytowaæ plik /etc/wmtunerc (albo go 
skopiowaæ do ~./home/.wmtunerc i tam wyedytowaæ) aby ustawiæ odpowiedni 
adres radia na karcie i ustawiæ stacje. Dobrej zabawy !

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}} \
	$RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install sample.wmtunerc $RPM_BUILD_ROOT%{_datadir}/wmtunerc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(4755,root,root) %{_bindir}/%{name}
%{_datadir}/wmtunerc
/etc/X11/applnk/DockApplets/%{name}.desktop
