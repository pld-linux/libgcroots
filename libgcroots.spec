#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Roots acquisition library for Garbage Collector
Summary(pl.UTF-8):	Biblioteka do wydobywania podstaw do odśmiecania pamięci
Name:		libgcroots
Version:	0.2.3
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: http://code.google.com/p/sigscheme/downloads/list
Source0:	http://sigscheme.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3c2e0ce9f8c09ad96aa88ebf15ac028d
URL:		http://code.google.com/p/sigscheme/wiki/libgcroots
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This library encourages to have own GC such as for
small-libgcrootstprint, some application-specific optimizations, just
learning or to test experimental ideas.

%description -l pl.UTF-8
libgcroots tworzy abstrakcję zależnych od architektury części
wydobywania podstaw do odśmiecania pomięci, takich jak okna rejestrów
procesora SPARC czy przestrzeń rejestrów na stosie IA64.

Biblioteka zachęca do używania własnego GC, jak w przypadku
small-libgcrootstprint, paru optymalizacji zależnych od aplikacji,
tylko nauki albo ekspertymentowania.

%package devel
Summary:	Header files for libgcroots library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgcroots
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgcroots library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgcroots.

%package static
Summary:	Static libgcroots library
Summary(pl.UTF-8):	Statyczna biblioteka libgcroots
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgcroots library.

%description static -l pl.UTF-8
Statyczna biblioteka libgcroots.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libgcroots.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgcroots.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgcroots.so
%{_includedir}/gcroots.h
%{_includedir}/libgcroots
%{_pkgconfigdir}/gcroots.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgcroots.a
%endif
