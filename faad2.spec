Summary:	Freeware Advanced Audio Decoder 2
Name:		faad2
Version:	2.7
Release:	4
License:	GPL
Group:		Applications/Sound
Source0:	http://heanet.dl.sourceforge.net/faac/%{name}-%{version}.tar.gz
# Source0-md5:	ee1b4d67ea2d76ee52c5621bc6dbf61e
Patch0:		%{name}-mpeg4ip.patch
Patch1:		%{name}-soname.patch
URL:		http://www.audiocoding.com/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder,
completely written from scratch.

%package libs
Summary:	FAAD 2 libraries
Group:		Libraries

%description libs
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder,
completely written from scratch. This package contains base FAAD 2
libraries: libfaad and libmp4ff.

%package devel
Summary:	Header files for faad2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for faad2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i -e 's|dnl AC_PROG_CXX|AC_PROG_CXX|g' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--without-xmms
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/faad

%files libs
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libfaad.so.?
%attr(755,root,root) %{_libdir}/libfaad.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfaad.so
%{_libdir}/libfaad.la
%{_includedir}/faad.h
%{_includedir}/neaacdec.h

