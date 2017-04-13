Summary:	An advanced molecular editor for chemical purposes
Name:		avogadro
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://downloads.sourceforge.net/avogadro/%{name}-%{version}.tar.gz
# Source0-md5:	3206068fc27bd3b717c568ee72f1e5ec
Patch0:		%{name}-linguist.patch
Patch1:		%{name}-cmake.patch
Patch2:		%{name}-moc-boost.patch
Patch3:		gcc6.patch
Patch4:		python-install.patch
URL:		http://avogadro.openmolecules.net/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	boost-devel >= 1.35
BuildRequires:	boost-python-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-utils
BuildRequires:	eigen >= 1:2.0.12
BuildRequires:	glew-devel >= 1.5.0
BuildRequires:	openbabel-devel >= 2.2.2
BuildRequires:	pkgconfig
BuildRequires:	python-numpy-devel
BuildRequires:	python-sip-devel
BuildRequires:	qt4-build >= 4.8.2-5
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.8.2-5
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
Requires:	glew-devel

%description devel
This package contains files to develop applications using Avogadros
libraries.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
install -d build
cd build
%cmake \
	-DENABLE_GLSL=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_UPDATE_CHECKER=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	..

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/qt4/mkspecs/features

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/avopkg
%attr(755,root,root) %{_bindir}/qube
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}-icon.png
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/avogadro.1*
%{_mandir}/man1/avopkg.1*

%files devel
%defattr(644,root,root,755)
%{_datadir}/lib%{name}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_datadir}/qt4/mkspecs/features/avogadro.prf
%{_pkgconfigdir}/avogadro.pc

%files libs
%defattr(644,root,root,755)
%{py_sitedir}/Avogadro.so
%{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/*.so.*
