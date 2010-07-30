
%define		qtver	4.6.3

Summary:	An advanced molecular editor for chemical purposes
Name:		avogadro
Version:	1.0.0
Release:	0.1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://downloads.sourceforge.net/avogadro/%{name}-%{version}.tar.bz2
# fix build with sip 4.10
URL:		http://avogadro.openmolecules.net/
Patch0:		%{name}-sip.patch
Patch1:		%{name}-linguist.patch
BuildRequires:	boost-devel >= 1.35
BuildRequires:	cmake >= 2.8.0
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-utils
BuildRequires:	eigen >= 1:2.0.12
BuildRequires:	glew-devel >= 1.5.0
#BuildRequires:	numpy
BuildRequires:	openbabel-devel >= 2.2.2
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	sip
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials
science, and related areas, which offers flexible rendering and a
powerful plugin architecture.

%package libs
Summary:	Shared libraries for Avogadro
Group:		Libraries

%description libs
This package contains the shared libraries for the molecular editor
Avogadro.

%package devel
Summary:	Development files for Avogadro
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains files to develop applications using Avogadros
libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
install -d build
cd build
%cmake \
	-DENABLE_GLSL=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_UPDATE_CHECKER=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}-icon.png
%{_desktopdir}/%{name}.desktop

%files devel
%defattr(644,root,root,755)
%{_datadir}/lib%{name}
%{_includedir}/%{name}
%{_libdir}/*.so

%files libs
%defattr(644,root,root,755)
%{py_sitedir}/Avogadro.so
%{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/*.so.*
