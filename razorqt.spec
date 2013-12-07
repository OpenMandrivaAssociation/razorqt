%define qtxdglibdevel	%mklibname qtxdg -d
%define libnamedevel	%mklibname  %name -d
%define oname		razor

Name:		%{oname}qt
Version:	0.5.2
Release:	4
License:	LGPLv2+
Source0:	https://github.com/downloads/Razor-qt/razor-qt/%{name}-%{version}.tar.bz2
Group:		Graphical desktop/Other
Summary:	Razor is a lightweight desktop toolbox
Url:		http://%{oname}-qt.org

Patch0:		%{oname}-panel-quicklaunch.patch
Patch1:		razorqt-0.5.2-fix-build-with-latest-lightdm.patch

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	magic-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(polkit-qt-1)
BuildRequires:	pkgconfig(liblightdm-qt-3)
BuildRequires:	pkgconfig(polkit-qt-agent-1)
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
%_libdir/lib%{oname}mount.so.%{librazormount_major}*

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
%_libdir/lib%{oname}qt.so.%{librazorqt_major}*

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
%doc libraries/%{oname}qxt/LICENSE
%_libdir/lib%{oname}qxt.so.%{librazorqxt_major}*

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
%{_libdir}/lib%{oname}*.so
%{_includedir}/%{oname}*/
%{_bindir}/%{oname}-x11info
%{_libdir}/pkgconfig/%{oname}mount.pc
%{_libdir}/pkgconfig/%{oname}qxt.pc
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
%{_bindir}/%{oname}-appswitcher

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
%{_bindir}/%{oname}-desktop
%{_libdir}/%{oname}-desktop
%dir %{_datadir}/%{oname}
%{_sysconfdir}/%{oname}/desktop.conf
%{_datadir}/%{oname}/%{oname}-desktop/

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
%{_bindir}/%{oname}-panel
%{_libdir}/%{oname}-panel/
%{_datadir}/%{oname}/%{oname}-panel/
%{_sysconfdir}/%{oname}/%{oname}-panel/panel.conf

#--------------------------------------------------------------------

%package	data
Summary:	RazorQt resources and shared data
Group:		Graphical desktop/Other

Conflicts:	%{name}-data <= 0.4.1
Obsoletes:	%{name}-data <= 0.4.1

%description    data
%{summary}

%files		data
%dir %{_datadir}/%{oname}
%dir %{_datadir}/%{oname}/themes
%dir %{_datadir}/%{oname}/graphics
%{_sysconfdir}/%{oname}/%{oname}.conf
%{_datadir}/%{oname}/graphics/*
%{_datadir}/%{oname}/themes/*
%config %_sysconfdir/xdg/menus/%{oname}-applications.menu
%config %_sysconfdir/xdg/autostart/*.desktop
%config %_sysconfdir/%{oname}/windowmanagers.conf
%{_datadir}/desktop-directories/%{oname}*
%{_datadir}/lib%{name}
%{_datadir}/libqtxdg/
# temp files - it will be removed when it becomes part of upstream
%{_libdir}/%{oname}-xdg-tools
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
%{_bindir}/%{oname}-autosuspend
#% {_datadir}/applications/% {oname}-autosuspend.desktop
%dir %{_datadir}/%{oname}/%{oname}-autosuspend
%{_datadir}/%{oname}/%{oname}-autosuspend/*
%{_iconsdir}/hicolor/scalable/apps/%{oname}-autosuspend.svg

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
%{_bindir}/%{oname}-power
%dir %{_datadir}/%{oname}/%{oname}-power
%{_datadir}/%{oname}/%{oname}-power/*.qm
%{_datadir}/applications/%{oname}-power.desktop

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
%{_bindir}/%{oname}-runner
%dir %{_datadir}/%{oname}/%{oname}-runner
%{_datadir}/%{oname}/%{oname}-runner/*

#--------------------------------------------------------------------

%package	notificationd
Summary:	RazorQt notification system
Group:		Graphical desktop/Other
Requires:	%{name}-config-notificationd

%description	notificationd
%{summary}

%files		notificationd
%{_bindir}/%{oname}-notificationd
%{_datadir}/%{oname}/%{oname}-notificationd/*.qm

#--------------------------------------------------------------------

%package	globalkeyshortcuts
Summary:	RazorQt global key shortcuts system
Group:		Graphical desktop/Other
Requires:	%{name}-config-globalkeyshortcuts

%description	globalkeyshortcuts
%{summary}

%files		globalkeyshortcuts
%{_bindir}/%{oname}-globalkeyshortcuts

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
%{_bindir}/%{oname}-session
%{_bindir}/%{oname}-about
%{_bindir}/%{oname}-openssh-askpass
%{_datadir}/%{oname}/%{oname}-openssh-askpass/%{oname}-openssh-askpass*.qm
%{_bindir}/start%{oname}
%{_datadir}/applications/%{oname}-about.desktop
%{_sysconfdir}/%{oname}/session.conf
%dir %{_datadir}/%{oname}/%{oname}-session
%{_datadir}/%{oname}/%{oname}-session/*
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
%{_bindir}/%{oname}-config
%{_datadir}/applications/%{oname}-config.desktop
%{_datadir}/applications/%{oname}-config-qtconfig.desktop
%config %_sysconfdir/xdg/menus/%{oname}-config.menu
%dir %{_datadir}/%{oname}/%{oname}-config
%{_datadir}/%{oname}/%{oname}-config/razor-config-appearance*.qm
%{_datadir}/%{oname}/%{oname}-config/%{oname}-config_*.qm

#--------------------------------------------------------------------

%package	config-globalkeyshortcuts
Summary:	RazorQt globalkeyshortcuts configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-globalkeyshortcuts
%{summary}

%files		config-globalkeyshortcuts	
%{_bindir}/%{oname}-config-globalkeyshortcuts
%{_datadir}/applications/%{oname}-config-globalkeyshortcuts.desktop
%{_datadir}/%{oname}/%{oname}-config-globalkeyshortcuts/%{oname}-config-globalkeyshortcuts*.qm

#--------------------------------------------------------------------

%package	config-notificationd
Summary:	RazorQt notificationd configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-notificationd
%{summary}

%files		config-notificationd	
%{_bindir}/%{oname}-config-notificationd
%{_datadir}/applications/%{oname}-config-notificationd.desktop
%{_datadir}/%{oname}/%{oname}-config-notificationd/*.qm

#--------------------------------------------------------------------

%package	config-desktop
Summary:	RazorQt desktop configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-desktop
%{summary}

%files		config-desktop	
%{_bindir}/%{oname}-config-desktop
%{_datadir}/applications/%{oname}-config-desktop.desktop


#--------------------------------------------------------------------

%package	config-autosuspend
Summary:	RazorQt autosuspend configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-autosuspend
%{summary}

%files		config-autosuspend	
%{_bindir}/%{oname}-config-autosuspend
%{_datadir}/applications/%{oname}-config-autosuspend.desktop
%{_datadir}/%{oname}/%{oname}-config-autosuspend/%{oname}-config-autosuspend*.qm

#--------------------------------------------------------------------

%package	config-session
Summary:	RazorQt session configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}

%description	config-session
%{summary}

%files		config-session	
%{_bindir}/%{oname}-config-session
%{_datadir}/applications/%{oname}-config-session.desktop
%dir %{_datadir}/%{oname}/%{oname}-config-session
%{_datadir}/%{oname}/%{oname}-config-session/*

#--------------------------------------------------------------------

%package	config-mouse
Summary:	RazorQt mouse configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}
License:	GPLv2 or GPLv3

%description	config-mouse
%{summary}

%files		config-mouse	
%{_bindir}/%{oname}-config-mouse
%{_datadir}/applications/%{oname}-config-mouse.desktop
%{_datadir}/%{oname}/%{oname}-config/%{oname}-config-mouse*.qm

#--------------------------------------------------------------------

%package	config-appearance
Summary:	RazorQt appearance configuration tool
Group:		Graphical desktop/Other
Requires:	%{name}-config = %{version}-%{release}
License:	LGPLv2+

%description	config-appearance
%{summary}

%files		config-appearance	
%{_bindir}/%{oname}-config-appearance
%{_datadir}/applications/%{oname}-config-appearance.desktop


#--------------------------------------------------------------------

%package	confupdate
Summary:	RazorQt configuration update tool
Requires:	%{name}-data = %{version}-%{release}

Conflicts:	%{name}-confupdate <= 0.4.1
Obsoletes:	%{name}-confupdate <= 0.4.1

%description	confupdate
Tool to update configuration from razorqt version 0.4.1 to 0.5.0

%files		confupdate
%{_bindir}/%{oname}-confupdate
%dir %{_datadir}/%{oname}/%{oname}-confupdate
%{_datadir}/%{oname}/%{oname}-confupdate/desktop-041-050.py
%{_datadir}/%{oname}/%{oname}-confupdate/%{oname}-0.5.upd
%{_libdir}/%{oname}-confupdate_bin/sesion_modules

#--------------------------------------------------------------------

%package	policykit-agent
Summary:	RazorQt policykit integration
Group:		System/X11

%description policykit-agent
RazorQt policykit integration.

%files policykit-agent
%{_datadir}/%{oname}/%{oname}-policykit-agent/%{oname}-policykit-agent*.qm
%{_bindir}/razor-policykit-agent

#--------------------------------------------------------------------
%package -n	lightdm-%{name}-greeter
Summary:	LightDM greeter that uses the Razor-qt (Qt based) lib kit
Group:		Graphical desktop/Other
Provides:	lightdm-greeter
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-power = %{version}-%{release}
Requires:	lightdm

%description -n lightdm-%{name}-greeter
A LightDM greeter that uses the Razor-qt and Qt libraries, it was written
for Razor-qt but it can be used standalone as well.

This package is part of the Razor-qt.

%files -n lightdm-%{name}-greeter
%{_bindir}/razor-lightdm-greeter
%{_datadir}/xgreeters/lightdm-razor-greeter.desktop
%{_datadir}/%{oname}/%{oname}-lightdm-greeter/%{oname}-lightdm-greeter_*.qm

%post -n lightdm-%{name}-greeter
%{_sbindir}/update-alternatives \
	--install %{_datadir}/xgreeters/lightdm-greeter.desktop \
	lightdm-greeter \
	%{_datadir}/xgreeters/lightdm-razor-greeter.desktop \
	10

%postun -n lightdm-%{name}-greeter
if [ $1 -eq 0 ]; then
%{_sbindir}/update-alternatives \
	--remove lightdm-greeter \
	%{_datadir}/xgreeters/lightdm-razor-greeter.desktop
fi

%prep
%setup -q
%apply_patches
# silence rpmlint's complains about non-readable
# source files in debuginfo
find . -name "*.cpp" -o -name "*.h" -o -name LICENSE |xargs chmod 0644

%build
%cmake_qt4
%make 


%install
%makeinstall_std -C build

for i in `find %{buildroot}%{_datadir}/applications/ -type f -name "*.desktop"`;
do
	desktop-file-validate $i
done

#========================================
# the session file

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
outfile=%{buildroot}%{_sysconfdir}/X11/wmsession.d/05%{oname}

cat > $outfile << EOF
NAME=RazorDesktop
DESC=The RazorQt Desktop Environment
EXEC=/usr/bin/start%{oname}
SCRIPT:
exec /usr/bin/start%{oname}

EOF

rm -f %{buildroot}%{_datadir}/apps/kdm/sessions/*.desktop
rm -f %{buildroot}%{_datadir}/xsessions/*.desktop
