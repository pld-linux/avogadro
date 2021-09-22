Summary:	An advanced molecular editor for chemical purposes
Summary(pl.UTF-8):	Zaawansowany edytor molekularny do zastosowań chemicznych
Name:		avogadro
Version:	1.2.0
Release:	12
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://downloads.sourceforge.net/avogadro/%{name}-%{version}.tar.gz
# Source0-md5:	3206068fc27bd3b717c568ee72f1e5ec
Patch1:		%{name}-cmake.patch
Patch2:		%{name}-moc-boost.patch
Patch3:		gcc6.patch
Patch4:		python-install.patch
Patch5:		avogadro_eigen3.patch
Patch6:		boost-python.patch
URL:		http://avogadro.openmolecules.net/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	QtCore-devel >= 4.6.0
BuildRequires:	QtGui-devel >= 4.6.0
BuildRequires:	QtNetwork-devel >= 4.6.0
BuildRequires:	QtOpenGL-devel >= 4.6.0
BuildRequires:	boost-devel >= 1.37.0
BuildRequires:	boost-python-devel >= 1.37.0
BuildRequires:	cmake >= 2.8.11
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-utils
BuildRequires:	eigen3
BuildRequires:	glew-devel >= 1.5.0
BuildRequires:	libstdc++-devel
BuildRequires:	openbabel-devel >= 2.2.2
BuildRequires:	pkgconfig
BuildRequires:	python-numpy-devel
BuildRequires:	python-sip
BuildRequires:	python-sip-devel
BuildRequires:	qt4-build >= 4.8.2-5
BuildRequires:	qt4-linguist >= 4.8.2-5
BuildRequires:	qt4-qmake >= 4.8.2-5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials
science, and related areas, which offers flexible rendering and a
powerful plugin architecture.

%description -l pl.UTF-8
Zaawansowany edytor molekularny, zaprojektowany pod kątem zastosowań
na wielu platformach komputerowych w chemii obliczeniowej, modelowaniu
cząsteczek, bioinformatyce, materiałoznawstwie i pochodnych obszarach.
Oferuje elastyczne renderowanie oraz funkcjonalną architekturę
wtyczek.

%package libs
Summary:	Shared libraries for Avogadro
Summary(pl.UTF-8):	Biblioteki współdzielone Avogadro
Group:		Libraries

%description libs
This package contains the shared libraries for the molecular editor
Avogadro.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone dla edytora molekularnego
Avogadro.

%package devel
Summary:	Development files for Avogadro
Summary(pl.UTF-8):	Pliki programistyczne Avogadro
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glew-devel

%description devel
This package contains files to develop applications using Avogadro
libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki do tworzenia aplikacji przy użyciu bibliotek
Avogadro.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
install -d build
cd build
export QTDIR=%{_libdir}/qt4
%cmake .. \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}" \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_GLSL=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_UPDATE_CHECKER=OFF \
	-DINSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/libmsym \
	-DINSTALL_LIB_DIR:PATH=%{_lib}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/qt4/mkspecs/features

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/avogadro
%attr(755,root,root) %{_bindir}/avopkg
%attr(755,root,root) %{_bindir}/qube
%attr(755,root,root) %{_libdir}/avogadro/1_2/colors/*.so
%attr(755,root,root) %{_libdir}/avogadro/1_2/engines/*.so
%attr(755,root,root) %{_libdir}/avogadro/1_2/extensions/*.so
%attr(755,root,root) %{_libdir}/avogadro/1_2/tools/*.so
%{_datadir}/%{name}/builder
%{_datadir}/%{name}/crystals
%{_datadir}/%{name}/fragments
%lang(af) %{_datadir}/%{name}/i18n/avogadro_af.qm
%lang(ar) %{_datadir}/%{name}/i18n/avogadro_ar.qm
%lang(bg) %{_datadir}/%{name}/i18n/avogadro_bg.qm
%lang(ca) %{_datadir}/%{name}/i18n/avogadro_ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/i18n/avogadro_ca@valencia.qm
%lang(cs) %{_datadir}/%{name}/i18n/avogadro_cs.qm
%lang(da) %{_datadir}/%{name}/i18n/avogadro_da.qm
%lang(de) %{_datadir}/%{name}/i18n/avogadro_de.qm
%lang(el) %{_datadir}/%{name}/i18n/avogadro_el.qm
%lang(en_AU) %{_datadir}/%{name}/i18n/avogadro_en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/i18n/avogadro_en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/i18n/avogadro_en_GB.qm
%lang(es) %{_datadir}/%{name}/i18n/avogadro_es.qm
%lang(et) %{_datadir}/%{name}/i18n/avogadro_et.qm
%lang(eu) %{_datadir}/%{name}/i18n/avogadro_eu.qm
%lang(fi) %{_datadir}/%{name}/i18n/avogadro_fi.qm
%lang(fr) %{_datadir}/%{name}/i18n/avogadro_fr.qm
%lang(fr_CA) %{_datadir}/%{name}/i18n/avogadro_fr_CA.qm
%lang(gl) %{_datadir}/%{name}/i18n/avogadro_gl.qm
%lang(he) %{_datadir}/%{name}/i18n/avogadro_he.qm
%lang(hi) %{_datadir}/%{name}/i18n/avogadro_hi.qm
%lang(hr) %{_datadir}/%{name}/i18n/avogadro_hr.qm
%lang(hu) %{_datadir}/%{name}/i18n/avogadro_hu.qm
%lang(id) %{_datadir}/%{name}/i18n/avogadro_id.qm
%lang(it) %{_datadir}/%{name}/i18n/avogadro_it.qm
%lang(ja) %{_datadir}/%{name}/i18n/avogadro_ja.qm
%lang(kn) %{_datadir}/%{name}/i18n/avogadro_kn.qm
%lang(ko) %{_datadir}/%{name}/i18n/avogadro_ko.qm
%lang(ms) %{_datadir}/%{name}/i18n/avogadro_ms.qm
%lang(nb) %{_datadir}/%{name}/i18n/avogadro_nb.qm
%lang(nl) %{_datadir}/%{name}/i18n/avogadro_nl.qm
%lang(oc) %{_datadir}/%{name}/i18n/avogadro_oc.qm
%lang(pl) %{_datadir}/%{name}/i18n/avogadro_pl.qm
%lang(pt) %{_datadir}/%{name}/i18n/avogadro_pt.qm
%lang(pt_BR) %{_datadir}/%{name}/i18n/avogadro_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/i18n/avogadro_ru.qm
%lang(sk) %{_datadir}/%{name}/i18n/avogadro_sk.qm
%lang(sl) %{_datadir}/%{name}/i18n/avogadro_sl.qm
%lang(sq) %{_datadir}/%{name}/i18n/avogadro_sq.qm
%lang(sr) %{_datadir}/%{name}/i18n/avogadro_sr.qm
%lang(sv) %{_datadir}/%{name}/i18n/avogadro_sv.qm
%lang(ta) %{_datadir}/%{name}/i18n/avogadro_ta.qm
%lang(te) %{_datadir}/%{name}/i18n/avogadro_te.qm
%lang(th) %{_datadir}/%{name}/i18n/avogadro_th.qm
%lang(tr) %{_datadir}/%{name}/i18n/avogadro_tr.qm
%lang(ug) %{_datadir}/%{name}/i18n/avogadro_ug.qm
%lang(uk) %{_datadir}/%{name}/i18n/avogadro_uk.qm
%lang(vi) %{_datadir}/%{name}/i18n/avogadro_vi.qm
%lang(zh_CN) %{_datadir}/%{name}/i18n/avogadro_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/i18n/avogadro_zh_TW.qm
%{_pixmapsdir}/avogadro-icon.png
%{_desktopdir}/avogadro.desktop
%{_mandir}/man1/avogadro.1*
%{_mandir}/man1/avopkg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavogadro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavogadro.so.1
%attr(755,root,root) %{_libdir}/libavogadro_OpenQube.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavogadro_OpenQube.so.0
%attr(755,root,root) %{_libdir}/libmsym.so
%dir %{_libdir}/avogadro
%dir %{_libdir}/avogadro/1_2
%dir %{_libdir}/avogadro/1_2/colors
%dir %{_libdir}/avogadro/1_2/engines
%dir %{_libdir}/avogadro/1_2/extensions
%dir %{_libdir}/avogadro/1_2/tools
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n
%lang(ar) %{_datadir}/%{name}/i18n/libavogadro_ar.qm
%lang(bg) %{_datadir}/%{name}/i18n/libavogadro_bg.qm
%lang(bs) %{_datadir}/%{name}/i18n/libavogadro_bs.qm
%lang(ca) %{_datadir}/%{name}/i18n/libavogadro_ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/i18n/libavogadro_ca@valencia.qm
%lang(cs) %{_datadir}/%{name}/i18n/libavogadro_cs.qm
%lang(da) %{_datadir}/%{name}/i18n/libavogadro_da.qm
%lang(de) %{_datadir}/%{name}/i18n/libavogadro_de.qm
%lang(el) %{_datadir}/%{name}/i18n/libavogadro_el.qm
%lang(en_AU) %{_datadir}/%{name}/i18n/libavogadro_en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/i18n/libavogadro_en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/i18n/libavogadro_en_GB.qm
%lang(es) %{_datadir}/%{name}/i18n/libavogadro_es.qm
%lang(et) %{_datadir}/%{name}/i18n/libavogadro_et.qm
%lang(eu) %{_datadir}/%{name}/i18n/libavogadro_eu.qm
%lang(fi) %{_datadir}/%{name}/i18n/libavogadro_fi.qm
%lang(fr) %{_datadir}/%{name}/i18n/libavogadro_fr.qm
%lang(gl) %{_datadir}/%{name}/i18n/libavogadro_gl.qm
%lang(he) %{_datadir}/%{name}/i18n/libavogadro_he.qm
%lang(hi) %{_datadir}/%{name}/i18n/libavogadro_hi.qm
%lang(hu) %{_datadir}/%{name}/i18n/libavogadro_hu.qm
%lang(id) %{_datadir}/%{name}/i18n/libavogadro_id.qm
%lang(it) %{_datadir}/%{name}/i18n/libavogadro_it.qm
%lang(ja) %{_datadir}/%{name}/i18n/libavogadro_ja.qm
%lang(kn) %{_datadir}/%{name}/i18n/libavogadro_kn.qm
%lang(ko) %{_datadir}/%{name}/i18n/libavogadro_ko.qm
%lang(ms) %{_datadir}/%{name}/i18n/libavogadro_ms.qm
%lang(nb) %{_datadir}/%{name}/i18n/libavogadro_nb.qm
%lang(nl) %{_datadir}/%{name}/i18n/libavogadro_nl.qm
%lang(oc) %{_datadir}/%{name}/i18n/libavogadro_oc.qm
%lang(pl) %{_datadir}/%{name}/i18n/libavogadro_pl.qm
%lang(pt) %{_datadir}/%{name}/i18n/libavogadro_pt.qm
%lang(pt_BR) %{_datadir}/%{name}/i18n/libavogadro_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/i18n/libavogadro_ru.qm
%lang(sk) %{_datadir}/%{name}/i18n/libavogadro_sk.qm
%lang(sl) %{_datadir}/%{name}/i18n/libavogadro_sl.qm
%lang(sq) %{_datadir}/%{name}/i18n/libavogadro_sq.qm
%lang(sr) %{_datadir}/%{name}/i18n/libavogadro_sr.qm
%lang(sv) %{_datadir}/%{name}/i18n/libavogadro_sv.qm
%lang(th) %{_datadir}/%{name}/i18n/libavogadro_th.qm
%lang(tr) %{_datadir}/%{name}/i18n/libavogadro_tr.qm
%lang(ug) %{_datadir}/%{name}/i18n/libavogadro_ug.qm
%lang(uk) %{_datadir}/%{name}/i18n/libavogadro_uk.qm
%lang(vi) %{_datadir}/%{name}/i18n/libavogadro_vi.qm
%lang(zh) %{_datadir}/%{name}/i18n/libavogadro_zh_CN.qm
%lang(zh) %{_datadir}/%{name}/i18n/libavogadro_zh_TW.qm
# %files -n python-avogadro ?
%attr(755,root,root) %{py_sitedir}/Avogadro.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavogadro.so
%attr(755,root,root) %{_libdir}/libavogadro_OpenQube.so
%{_includedir}/avogadro
%{_includedir}/libmsym
%{_datadir}/libavogadro
%{_datadir}/qt4/mkspecs/features/avogadro.prf
%{_libdir}/avogadro/Avogadro*.cmake
%{_libdir}/avogadro/1_2/AvogadroUse.cmake
%{_libdir}/avogadro/1_2/cmake
%{_libdir}/cmake/libmsym
%{_pkgconfigdir}/avogadro.pc
