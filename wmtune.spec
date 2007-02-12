Summary:	Window Maker Dockable Applet for Sound Cards with FM Radio
Summary(pl.UTF-8):   Dokowalny aplet dla Window Makera do kart muzycznych z radiem
Name:		wmtune
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.mezaway.org/pub/DockApps/%{name}-%{version}.tar.gz
# Source0-md5:	fa1589473e46294024238ac82d2e41e3
Source1:	%{name}.desktop
Patch0:		%{name}-SB16_FM.patch
Patch1:		%{name}-opts.patch
URL:		http://windowmaker.mezaway.org/dockapps/wmtune.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows user to hear radio stations and to set an alarm if
his soundcard support this. I've patched the original source to get
scannig and tunning up and down on my Vibra16FM soundcard. After
installation you must edit your /etc/wmtunerc file (or copy it to
~./home/.wmtunerc and edit there) to set up proper I/O radio on your
card address and to set up the stations. Enjoy it!

%description -l pl.UTF-8
Program ten umożliwia używanie radia na karcie dźwiękowej oraz
ustawianie alarmu, jeżeli karta to umożliwia. Autor zmienił nieco
oryginalne źródła aby uzyskać przestrajanie i wyszukiwanie stacji na
swojej karcie Vibra16FM. Po instalacji należy zmodyfikować plik
/etc/wmtunerc (albo go skopiować do ~./home/.wmtunerc i tam
poprawić) aby ustawić odpowiedni adres radia na karcie i ustawić
stacje. Dobrej zabawy!

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install sample.wmtunerc $RPM_BUILD_ROOT%{_datadir}/wmtunerc
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README sample.wmtunerc
%attr(4755,root,root) %{_bindir}/%{name}
%{_datadir}/wmtunerc
%{_desktopdir}/docklets/%{name}.desktop
