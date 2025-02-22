%define name downman
%define version 0.0.5
%define release %mkrel 9

Name:		%name
Summary:	Download manager for gnome
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		https://downman.sourceforge.net/
Group:		Networking/File transfer
Source0:	%{name}-%{version}.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
Patch0:		downman-gcc4.patch
Patch1:		downman-0.0.5-fix-link.patch
Patch2:		downman-0.0.5-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	automake >= 1.4
BuildRequires:	libgnome2-devel >= 2.0
BuildRequires:	libgnomeui2-devel >= 2.0
BuildRequires:	libglib2.0-devel >= 2.0
BuildRequires:	libglade2.0-devel >= 2.0

%description
Downman is a download manager for gnome.
It comes with a daemon, a gui and a monitor.

%prep
%setup -q
%patch0 -p0 -b .gcc4
%patch1 -p0 -b .link
%patch2 -p0 -b .str

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png

%find_lang %name 

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root,0755)
%doc NEWS
%{_bindir}/*
#%{_datadir}/locale/*/LC_MESSAGES/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/gdownman
%{_datadir}/applications/gdownman.desktop
%{_datadir}/pixmaps/gdownman.png


