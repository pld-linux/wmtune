Summary:	Window Maker Dockable Applet for Sound Cards with FM Radio
Summary(pl):	Dokowalny aplet dla Window Makera'a do kart muzycznych z radiem
Name:		wmtune
Version:	1.0
Release:	1
Copyright:	GPL
Vendor:		PLD
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
Packager:	Jacek Rz�sista <jacek@samm.com.pl>
Distribution:	PLD
URL:		http://windowmaker.mezaway.org/dockapps/wmtune.html
Source:		ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig 
Patch:		%{name}-SB16_FM.patch
BuildRoot:	/tmp/%{name}-%{version}
ExclusiveArch:	i386 i486 i586 i686

%description
This program allows user to hear radio stations and to set an alarm
if his soundcard support this. I've patched the original source to get
scannig and tunning up and down on my Vibra16FM soundcard. After
installation you must edit your /usr/local/etc/wmtunerc file (or copy 
it to ~./home/.wmtunerc and edit there) to set up proper I/O radio on 
your card address and to set up the stations. Enjoy it !

%description -l pl
Program ten umo�liwia u�ywanie radia na karcie d�wi�kowej oraz ustawianie
alarmu, je�eli karta to umo�liwia. Zmieni�em nieco oryginalne �r�d�a aby
uzyska� przestrajanie i wyszukiwanie stacji na mojej karcie Vibra16FM.
Po instalacji nale�y wyedytowa� plik /usr/local/etc/wmtunerc (albo go 
skopiowa� do ~./home/.wmtunerc i tam wyedytowa�) aby ustawi� odpowiedni 
adres radia na karcie i ustawi� stacje. Dobrej zabawy !

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/local/bin
install -d $RPM_BUILD_ROOT/usr/local/etc
install -d $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -s  %{name} $RPM_BUILD_ROOT/usr/local/bin
install sample.wmtunerc $RPM_BUILD_ROOT/usr/local/etc/wmtunerc

gzip -9nf README COPYING

install README.gz $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install COPYING.gz $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmtune

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
%attr(4755,root,root) /usr/local/bin/%{name}
%doc {README,COPYING}.gz
/usr/local/etc/wmtunerc
/etc/X11/wmconfig/wmtune

%changelog
* Wed Jul 20 1999 Jacek Rz�sista <jacek@samm.com.pl>
- initial RPM release
