%define qtxdglibdevel	%mklibname qtxdg -d
%define libnamedevel	%mklibname  %name -d
%define _name		razor

Name:		%{_name}qt
Version:	0.5.2
Release:	2
License:	LGPLv2+
Source0:	https://github.com/downloads/Razor-qt/razor-qt/%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Other
Summary:	Razor is a lightweight desktop toolbox
Url:		http://%{_name}-qt.org

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	magic-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(polkit-qt-1)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libstatgrab)
BuildRequires:	desktop-file-utils


%description
Razor-qt is an advanced, easy-to-use, and fast desktop environment based on 
Qt technologies. It has been tailored for users who value simplicity, speed, 
and an intuitive interface. 

#------------------------------------------------------------------------------

%define		librazormount_major 0
%define		librazormount %mklibname razormount %{librazormount_major}

%package -n	%librazormount
Summary:	RazorQt shared library
Group:		System/Libraries
License:	LGPLv2+

%description -n %librazormount
%{summary}

%files -n	%librazormount
%_libdir/lib%{_name}mount.so.%{librazormount_major}*

#------------------------------------------------------------------------------

%define		librazorqt_major 0
%define		librazorqt %mklibname razorqt %{librazorqt_major}

%package -n	%librazorqt
Summary:	RazorQt shared library
Group:		System/Libraries
License:	LGPLv2+

%description -n %librazorqt
%{summary}

%files -n	%librazorqt
%_libdir/lib%{_name}qt.so.%{librazorqt_major}*

#------------------------------------------------------------------------------

%define		librazorqxt_major 0
%define		librazorqxt %mklibname razorqxt %{librazorqxt_major}

%package -n	%librazorqxt
Summary:	Customized part of the libqxt library
Group:		System/Libraries
# BSD3 (gpl2 and gpl3 compatible, as from http://fedoraproject.org/wiki/Licensing#SoftwareLicenses)
License:	BSD

%description -n %librazorqxt
%{summary}

%files -n	%librazorqxt
%doc libraries/%{_name}qxt/LICENSE
%_libdir/lib%{_name}qxt.so.%{librazorqxt_major}*

#------------------------------------------------------------------------------

%define		libqtxdg_major 0
%define		libqtxdg %mklibname qtxdg %{libqtxdg_major}

%package -n	%libqtxdg
Summary:	Xdg manipulation library using Qt4
Group:		System/Libraries
# qiconloader.cpp and qiconloader_p.h -> lgplv2
# xdg* files -> lgplv2+
License:	LGPLv2+

%description -n %libqtxdg
%{summary}

%files -n	%libqtxdg
%_libdir/libqtxdg.so.%{libqtxdg_major}*

#--------------------------------------------------------------------

%package -n     %libnamedevel
Summary:	RazorQt development package
Group:		Development/Other
Requires:	%librazormount = %{version}-%{release}
Requires:	%librazorqt = %{version}-%{release}
Requires:	%librazorqxt = %{version}-%{release}
License:	GPLv2 and LGPLv2+

%description -n %libnamedevel
%{summary}

%files -n	%libnamedevel
%{_libdir}/lib%{_name}*.so
%{_includedir}/%{_name}*/
%{_bindir}/%{_name}-x11info
%{_libdir}/pkgconfig/%{_name}mount.pc
%{_libdir}/pkgconfig/%{_name}qxt.pc
%{_libdir}/pkgconfig/%{name}.pc

#------------------------------------------------------------------------------

%package -n     %{qtxdglibdevel}
Summary:	Development files for QtXdg library
Group:		Development/Other
Requires:	%{libqtxdg} = %{version}-%{release}
License:	LGPLv2+

%description -n %{qtxdglibdevel}
%{summary}

%files -n	%{qtxdglibdevel}
%{_libdir}/libqtxdg.so
%{_includedir}/qtxdg/
%{_libdir}/pkgconfig/qtxdg.pc

#--------------------------------------------------------------------

%package	appswitcher
Summary:	RazorQt application switcher
Group:		System/X11
Requires:	%{name}-data = %{version}-%{release}
License:	LGPLv2+

Conflicts:	%{name}-appswitcher <= 0.4.1
Obsoletes:	%{name}-appswitcher <= 0.4.1

%description    appswitcher
%{summary}

%files		appswitcher
%{_bindir}/%{_name}-appswitcher

#--------------------------------------------------------------------

%package	desktop
Summary:	RazorQt desktop
Group:		Graphical desktop/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-config-desktop = %{version}-%{release}
License:	LGPLv2+

Conflicts:	%{name}-desktop <= 0.4.1
Obsoletes:	%{name}-desktop <= 0.4.1

%description    desktop
%{summary}

%files		desktop
%{_bindir}/%{_name}-desktop
%{_libdir}/%{_name}-desktop
%dir %{_datadir}/%{_name}
%{_sysconfdir}/%{_name}/desktop.conf
%{_datadir}/%{_name}/%{_name}-desktop/

#--------------------------------------------------------------------

%package	panel
Summary:	RazorQt panel
Group:		Graphical desktop/Other
License:	LGPLv2+
Requires:	%{name}-data  = %{version}-%{release}
Requires:	%{name}-config-appearance = %{version}-%{release}
Requires:	%{name}-config-mouse = %{version}-%{release}

Conflicts:	%{name}-panel <= 0.4.1
Obsoletes:	%{name}-panel <= 0.4.1

%description    panel
%{summary}

%files		panel
%{_bindir}/%{_name}-panel
%{_libdir}/%{_name}-panel/
%{_datadir}/%{_name}/%{_name}-panel/
%{_sysconfdir}/%{_name}/%{_name}-panel/panel.conf

#--------------------------------------------------------------------

%package	data
Summary:	RazorQt resources and shared data
Group:		Graphical desktop/Other

Conflicts:	%{name}-data <= 0.4.1
Obsoletes:	%{name}-data <= 0.4.1

%description    data
%{summary}

%files		data
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/themes
%dir %{_datadir}/%{_name}/graphics
%{_sysconfdir}/%{_name}/%{_name}.conf
%{_datadir}/%{_name}/graphics/*
%{_datadir}/%{_name}/themes/*
%config %_sysconfdir/xdg/menus/%{_name}-applications.menu
%config %_sysconfdir/xdg/autostart/*.desktop
%config %_sysconfdir/%{_name}/windowmanagers.conf
%{_datadir}/desktop-directories/%{_name}*
%{_datadir}/lib%{name}
%{_datadir}/libqtxdg/
# temp files - it will be removed when it becomes part of upstream
%{_libdir}/%{_name}-xdg-tools
%{_datadir}/icons/hicolor/scalable/apps/laptop-lid*

#--------------------------------------------------------------------

%package	autosuspend
Summary:	RazorQt autosuspend application
Group:		Graphical desktop/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-config-autosuspend = %{version}-%{release}
Requires:	%{name}-power = %{version}-%{release}
License:	LGPLv2+

%description	autosuspend
%{summary}

%files		autosuspend
%{_bindir}/%{_name}-autosuspend
#% {_datadir}/applications/% {_name}-autosuspend.desktop
%dir %{_datadir}/%{_name}/%{_name}-autosuspend
%{_datadir}/%{_name}/%{_name}-autosuspend/*
%{_iconsdir}/hicolor/scalable/apps/%{_name}-autosuspend.svg

#--------------------------------------------------------------------

%package	power
Summary:	RazorQt power application
Group:		Graphical desktop/Other
Requires:	%{name}-data = %{version}-%{release}
License:	LGPLv2+

Conflicts:	%{name}-power <= 0.4.1
Obsoletes:	%{name}-power <= 0.4.1

%description    power
%{summary}

%files		power
%{_bindir}/%{_name}-power
%dir %{_datadir}/%{_name}/%{_name}-power
%{_datadir}/%{_name}/%{_name}-power/*.qm
%{_datadir}/applications/%{_name}-power.desktop

#--------------------------------------------------------------------

%package	runner
Summary:	RazorQt runner application
Group:		Graphical desktop/Other
Requires:	%{name}-data = %{version}-%{release}
License:	LGPLv2+

Conflicts:	%{name}-runner <= 0.4.1
Obsoletes:	%{name}-runner <= 0.4.1

%description    runner
%{summary}

%files		runner
%{_bindir}/%{_name}-runner
%dir %{_datadir}/%{_name}/%{_name}-runner
%{_datadir}/%{_name}/%{_name}-runner/*

#--------------------------------------------------------------------

%package	notificationd
Summary:	RazorQt notification system
Group:		Graphical desktop/Other
Requires:	%{name}-config-notificationd

%description	notificationd
%{summary}

%files		notificationd
%{_bindir}/%{_name}-notificationd
%{_datadir}/%{_name}/%{_name}-notificationd/*.qm

#--------------------------------------------------------------------

%package	globalkeyshortcuts
Summary:	RazorQt global key shortcuts system
Group:		Graphical desktop/Other
Requires:	%{name}-config-globalkeyshortcuts

%description	globalkeyshortcuts
%{summary}

%files		globalkeyshortcuts
%{_bindir}/%{_name}-globalkeyshortcuts

#--------------------------------------------------------------------

%package	session
Summary:	RazorQt session
Group:		Graphical desktop/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-config-session = %{version}-%{release}
Requires:	%{name}-notificationd = %{version}-%{release}
Requires:	%{name}-globalkeyshortcuts = %{version}-%{release}
Requires:	openbox
License:	LGPLv2+

Conflicts:	%{name}-session <= 0.4.1
Obsoletes:	%{name}-session <= 0.4.1
Obsoletes:	%{name}-openbox <= %{version}, %{name}-wm <= %{version}

%description    session
%{summary}

%files		session
%{_bindir}/%{_name}-session
%{_bindir}/%{_name}-about
%{_bindir}/%{_name}-openssh-askpass
%{_datadir}/%{_name}/%{_name}-openssh-askpass/%{_name}-openssh-askpass*.qm
%{_bindir}/start%{_name}
%{_datadir}/applications/%{_name}-about.desktop
%{_sysconfdir}/%{_name}/session.conf
%dir %{_datadir}/%{_name}/%{_name}-session
%{_datadir}/%{_name}/%{_name}-session/*
%{_sysconfdir}/X11/wmsession.d/*

#--------------------------------------------------------------------

%package	config
Summary:	RazorQt config tools
Group:		Graphical desktop/Other
License:	LGPLv2+
Requires:	%{name}-data = %{version}-%{release}

Conflicts:	%{name}-config <= 0.4.1
Obsoletes:	%{name}-config <= 0.4.1

%description    config
%{summary}

%files		config
%{_bindir}/%{_name}-config
%{_datadir}/applications/%{_name}-config.desktop
%{_datadir}/applications/%{_name}-config-qtconfig.desktop
%config %_sysconfdir/xdg/menus/%{_name}-config.menu
%dir %{_datadir}/%{_name}/%{_name}-config
%{_datadir}/%{_name}/%{_name}-config/razor-config-appearance*.qm
%{_datadir}/%{_name}/%{_name}-config/%{_name}-config_*.qm

#--------------------------------------------------------------------

%package	config-globalkeyshortcuts
Summary:	RazorQt globalkeyshortcuts configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-globalkeyshortcuts
%{summary}

%files		config-globalkeyshortcuts	
%{_bindir}/%{_name}-config-globalkeyshortcuts
%{_datadir}/applications/%{_name}-config-globalkeyshortcuts.desktop
%{_datadir}/%{_name}/%{_name}-config-globalkeyshortcuts/%{_name}-config-globalkeyshortcuts*.qm

#--------------------------------------------------------------------

%package	config-notificationd
Summary:	RazorQt notificationd configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-notificationd
%{summary}

%files		config-notificationd	
%{_bindir}/%{_name}-config-notificationd
%{_datadir}/applications/%{_name}-config-notificationd.desktop
%{_datadir}/%{_name}/%{_name}-config-notificationd/*.qm

#--------------------------------------------------------------------

%package	config-desktop
Summary:	RazorQt desktop configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-desktop
%{summary}

%files		config-desktop	
%{_bindir}/%{_name}-config-desktop
%{_datadir}/applications/%{_name}-config-desktop.desktop


#--------------------------------------------------------------------

%package	config-autosuspend
Summary:	RazorQt autosuspend configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-autosuspend
%{summary}

%files		config-autosuspend	
%{_bindir}/%{_name}-config-autosuspend
%{_datadir}/applications/%{_name}-config-autosuspend.desktop
%{_datadir}/%{_name}/%{_name}-config-autosuspend/%{_name}-config-autosuspend*.qm

#--------------------------------------------------------------------

%package	config-session
Summary:	RazorQt session configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-session
%{summary}

%files		config-session	
%{_bindir}/%{_name}-config-session
%{_datadir}/applications/%{_name}-config-session.desktop
%dir %{_datadir}/%{_name}/%{_name}-config-session
%{_datadir}/%{_name}/%{_name}-config-session/*

#--------------------------------------------------------------------

%package	config-mouse
Summary:	RazorQt mouse configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}
License:	GPLv2 or GPLv3

%description	config-mouse
%{summary}

%files		config-mouse	
%{_bindir}/%{_name}-config-mouse
%{_datadir}/applications/%{_name}-config-mouse.desktop
%{_datadir}/%{_name}/%{_name}-config/%{_name}-config-mouse*.qm

#--------------------------------------------------------------------

%package	config-appearance
Summary:	RazorQt appearance configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}
License:	LGPLv2+

%description	config-appearance
%{summary}

%files		config-appearance	
%{_bindir}/%{_name}-config-appearance
%{_datadir}/applications/%{_name}-config-appearance.desktop


#--------------------------------------------------------------------

%package	confupdate
Summary:	RazorQt configuration update tool
Requires:	%{name}-data = %{version}-%{release}

Conflicts:	%{name}-confupdate <= 0.4.1
Obsoletes:	%{name}-confupdate <= 0.4.1

%description	confupdate
Tool to update configuration from razorqt version 0.4.1 to 0.5.0

%files		confupdate
%{_bindir}/%{_name}-confupdate
%dir %{_datadir}/%{_name}/%{_name}-confupdate
%{_datadir}/%{_name}/%{_name}-confupdate/desktop-041-050.py
%{_datadir}/%{_name}/%{_name}-confupdate/%{_name}-0.5.upd
%{_libdir}/%{_name}-confupdate_bin/sesion_modules

#--------------------------------------------------------------------

%package	policykit
Summary:	RazorQt policykit integration
Group:		System/X11

%description policykit
RazorQt policykit integration.

%files policykit
%{_datadir}/%{_name}/%{_name}-policykit-agent/%{_name}-policykit-agent*.qm
%{_bindir}/razor-policykit-agent

#--------------------------------------------------------------------

%prep
%setup -q
# silence rpmlint's complains about non-readable
# source files in debuginfo
find . -name "*.cpp" -o -name "*.h" -o -name LICENSE |xargs chmod 0644

%build
%cmake_qt4
%make 

#% find_lang %{name}

%install
%makeinstall_std -C build

for i in `find %{buildroot}%{_datadir}/applications/ -type f -name "*.desktop"`;
do
	desktop-file-validate $i
done

#========================================
# the session file

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
outfile=%{buildroot}%{_sysconfdir}/X11/wmsession.d/05%{_name}

cat > $outfile << EOF
NAME=RazorDesktop
DESC=The RazorQt Desktop Environment
EXEC=/usr/bin/start%{_name}
SCRIPT:
exec /usr/bin/start%{_name}

EOF

rm -f %{buildroot}%{_datadir}/apps/kdm/sessions/*.desktop
rm -f %{buildroot}%{_datadir}/xsessions/*.desktop
