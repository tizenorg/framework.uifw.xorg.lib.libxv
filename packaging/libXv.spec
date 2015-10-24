Summary: X.Org X11 libXv runtime library
Name:    libXv
Version: 1.0.10
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(videoproto) pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXv runtime library

%package devel
Summary: X.Org X11 libXv development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxv-devel

%description devel
X.Org X11 libXv development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc AUTHORS COPYING
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0

%files devel
%defattr(-,root,root,-)
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
#%dir %{_mandir}/man3x
#%{_mandir}/man3/*.3*