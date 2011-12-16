%define major 0
%define libname %mklibname qtxdglib %{major}
%define develname %mklibname qtxdglib -d

%define razorlibs %mklibname razorqt %{major}


Name:		razorqt
Version:	0.4.0
Release:	1
License:	LGPL
Source:		razorqt-%{version}.tar.bz2
Group:		Graphical desktop/Other
Summary:	Razor a lightweight desktop toolbox
Vendor:		Razor-qt team
Url:		http://razor-qt.org
BuildRequires:	gcc-c++ cmake make file-devel libqt4-devel qt4-linguist libxcomposite-devel
Requires:	%{name}-desktop = %{version}, %{name}-panel = %{version}, %{name}-session = %{version}
Requires:	%{name}-appswitcher = %{version}, %{name}-runner = %{version}
Requires:	%{name}-config = %{version}, %{name}-data = %{version}
Requires:	razorqtlibs qtxdglib
BuildRequires:	libudev-devel >= 128

#Recommends:	qterminal, juffed, ptbatterysystemtray, qlipper, qxkb, qasmixer, screengrab


%package	devel
Summary:	RazorQt development package
Url:		http://razor-qt.org
Group:		Development/C
Requires:	%{razolibs}
Obsoletes:	razorqt-x11info <= %{version}

%package -n	%{razorlibs}
Summary:	RazorQt shared library
Url:		http://razor-qt.org
Group:		System/Libraries
Requires:	upower
#Requires:	oxygen-icon-theme
# names before 0.4
Obsoletes:	razorqt-libs <= %{version}, librazorqt0 <= %{version}
Provides:	razorqtlibs = %{version}

%package	-n %{libname}
Url:		http://razor-qt.org
Summary:	QtXdg library
Group:		System/Libraries
Provides:	qtxdglib = %{version}

%package	-n %{develname}
Url:		http://razor-qt.org
Summary:	Development files for QtXdg library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	qtxdglib-devel = %{version}

%package	appswitcher
Url:		http://razor-qt.org
Summary:	RazorQt application switcher
Group:		System/X11
Requires:	%{name}-data

%package	desktop
Url:		http://razor-qt.org
Summary:	RazorQt desktop
Group:		Graphical desktop/Other
Requires:	%{name}-data

%package	panel
Url:		http://razor-qt.org
Summary:	RazorQt panel
Group:		System/X11
Requires:	%{name}-data xscreensaver

%package	data
Url:		http://razor-qt.org
Summary:	RazorQt resources and shared data
Group:		System/X11
Obsoletes:	%{name}-resources <= %{version}

%package	runner
Url:		http://razor-qt.org
Summary:	RazorQt runner application
Group:		System/X11
Requires:	%{name}-data

%package	session
Url:		http://razor-qt.org
Summary:	RazorQt session
Group:		System/X11
Requires:	%{name}-data, openbox
Obsoletes:	%{name}-openbox <= %{version}, %{name}-wm <= %{version}

%package	config
Url:		http://razor-qt.org
Summary:	RazorQt config tools
Group:		System/X11

%description
Description:	%{summary}

%description	-n %{razorlibs}
Description:	%{summary}

%description	-n %{libname}
Description:	Implementation of XDG standards in Qt.

%description    -n %{develname}
Description:	%{summary}

%description	devel
Description:	%{summary}

%description	appswitcher
Description:	%{summary}

%description	desktop
Description:	%{summary}

%description	panel
Description:	%{summary}

%description	data
Description:	%{summary}

%description	runner
Description:	%{summary}

%description	config
Description:	%{summary}

%description	session
Description:	%{summary}

%prep
%setup -q

%build
%cmake_qt4 '-DCMAKE_MODULE_LINKER_FLAGS:STRING=-Wl,--as-needed -Wl,-z,relro -Wl,-O1 -Wl,--build-id -Wl,--enable-new-dtags, -lX11' '-DCMAKE_SHARED_LINKER_FLAGS:STRING='
%make

%install
cd build/
%makeinstall_std

%files
%doc README

%files -n %{razorlibs}
%{_libdir}/librazor*.so.*
%{_datadir}/librazorqt

%files  -n %{libname}
%{_libdir}/libqtxdg.so.*
%{_datadir}/qtxdg

%files  -n %{develname}
%{_libdir}/libqtxdg.so
%{_includedir}/qtxdg/

%files	devel
%{_libdir}/librazor*.so
%{_includedir}/razor*/
%{_bindir}/razor-x11info

%files	appswitcher
%{_bindir}/razor-appswitcher

%files	desktop
%{_bindir}/razor-desktop
%{_bindir}/razor-config-desktop
%{_libdir}/razor-desktop
%{_datadir}/applications/razor-config-desktop.desktop
%dir %{_datadir}/razor
%{_datadir}/razor/desktop.conf
%{_datadir}/razor/razor-desktop/

%files	panel
%{_bindir}/razor-panel
%{_libdir}/razor-panel/
%{_datadir}/razor/razor-panel/

%files	runner
%{_bindir}/razor-runner
%{_datadir}/razor/razor-runner/

%files  config
%{_bindir}/razor-config
%{_bindir}/razor-config-mouse
%{_bindir}/razor-config-appearance
%{_datadir}/applications/razor-config.desktop
%{_datadir}/applications/razor-config-mouse.desktop
%{_datadir}/applications/razor-config-appearance.desktop
%{_datadir}/razor/razor-config/

%files	session
%{_bindir}/razor-session
%{_bindir}/razor-config-session
%{_bindir}/startrazor
%{_datadir}/xsessions/razor*.desktop
%dir %{_datadir}/apps/
%dir %{_datadir}/apps/kdm
%dir %{_datadir}/apps/kdm/sessions
%{_datadir}/apps/kdm/sessions/razor*.desktop
%{_datadir}/applications/razor-config-session.desktop
%{_datadir}/razor/session*.conf
%{_datadir}/razor/razor-session/

%files	data
%{_datadir}/razor/razor.conf
%{_datadir}/razor/graphics/
%{_datadir}/razor/themes/
%config /etc/xdg/menus/razor-applications.menu
%dir /etc/xdg/menus
%{_datadir}/desktop-directories/razor*
%dir %{_datadir}/desktop-directories
# temp files - it will be removed when it becomes part of upstream
%{_libdir}/razor-xdg-tools
