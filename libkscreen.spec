%define libname %{mklibname KF5Screen 5}
%define devname %{mklibname KF5Screen -d}
%define major %(echo %{version} |cut -d. -f1-3)

Summary:	Library for dealing with screen parameters
Name:		libkscreen5
Version:	5.1.0.1
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{major}/libkscreen-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(XCB)
BuildRequires:	cmake(X11)
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	cmake(X11_XCB)
BuildRequires:	qt5-devel
BuildRequires:	cmake
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	ninja

Requires:	%{libname} = %{EVRD}

%dependinglibpackage KF5Screen 5

%description
Library for dealing with screen parameters

%files
%{_libdir}/plugins/kf5/kscreen

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}

%files -n %{devname}
%{_includedir}/KF5/KScreen
%{_includedir}/KF5/kscreen_version.h
%{_libdir}/cmake/KF5Screen
%{_libdir}/libKF5Screen.so
%{_libdir}/pkgconfig/*.pc
%{_prefix}/mkspecs/modules/*

#----------------------------------------------------------------------------

%prep
%setup -qn libkscreen-%{major}

%build
%cmake -G Ninja
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

