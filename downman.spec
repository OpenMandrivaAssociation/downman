%define name downman
%define version 0.0.5
%define release %mkrel 5

Name:		%name
Summary:	Download manager for gnome
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://downman.sourceforge.net/
Group:		Networking/File transfer
Source0:	%{name}-%{version}.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
Patch0:		downman-gcc4.patch
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

%build
%configure
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

%post
%update_menus

%postun
%clean_menus

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


