Summary:	Window Maker Dockable Applet for Sound Cards with FM Radio
Summary(pl):	Dokowalny aplet dla Window Makera do kart muzycznych z radiem
Name:		wmtune
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-SB16_FM.patch
Patch1:		%{name}-opts.patch
URL:		http://windowmaker.mezaway.org/dockapps/wmtune.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
This program allows user to hear radio stations and to set an alarm if
his soundcard support this. I've patched the original source to get
scannig and tunning up and down on my Vibra16FM soundcard. After
installation you must edit your /etc/wmtunerc file (or copy it to
~./home/.wmtunerc and edit there) to set up proper I/O radio on your
card address and to set up the stations. Enjoy it!

%description -l pl
Program ten umo�liwia u�ywanie radia na karcie d�wi�kowej oraz
ustawianie alarmu, je�eli karta to umo�liwia. Zmieni�em nieco
oryginalne �r�d�a aby uzyska� przestrajanie i wyszukiwanie stacji na
mojej karcie Vibra16FM. Po instalacji nale�y wyedytowa� plik
/etc/wmtunerc (albo go skopiowa� do ~./home/.wmtunerc i tam
wyedytowa�) aby ustawi� odpowiedni adres radia na karcie i ustawi�
stacje. Dobrej zabawy!

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install sample.wmtunerc $RPM_BUILD_ROOT%{_datadir}/wmtunerc
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(4755,root,root) %{_bindir}/%{name}
%{_datadir}/wmtunerc
%{_applnkdir}/DockApplets/%{name}.desktop
