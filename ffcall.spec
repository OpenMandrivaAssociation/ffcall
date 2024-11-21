%define major 1
%define ffcallmajor 0
%define oldlibavcall	%mklibname avcall 1
%define libavcall	%mklibname avcall
%define oldlibcallback	%mklibname callback 1
%define libcallback	%mklibname callback
%define oldlibtrampoline %mklibname trampoline 1
%define libtrampoline	%mklibname trampoline
%define oldlibffcall	%mklibname ffcall 0
%define libffcall	%mklibname ffcall

%define devname		%mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		ffcall
Version:	2.5
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.gnu.org/software/lib%{name}
Source:		https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch0:		ffcall-make-jN.patch

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

#----------------------------------------------------------------------------

%package -n %{libavcall}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
%rename %{oldlibavcall}

%description -n %{libavcall}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libavcall}
%{_libdir}/libavcall.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcallback}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
%rename %{oldlibcallback}

%description -n %{libcallback}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libcallback}
%{_libdir}/libcallback.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libffcall}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
%rename %{oldlibffcall}

%description -n %{libffcall}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libffcall}
%{_libdir}/libffcall.so.%{ffcallmajor}*

#----------------------------------------------------------------------------
%package -n %{libtrampoline}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
%rename %{oldlibtrampoline}

%description -n %{libtrampoline}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libtrampoline}
%{_libdir}/libtrampoline.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for ffcall library
Group:		Development/C
Requires:	%{libavcall} = %{EVRD}
Requires:	%{libcallback} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for ffcall library.

%files -n %{devname}
%doc NEWS README PLATFORMS
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*
%{_defaultdocdir}/%{devname}/html

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n lib%{name}-%{version}

%conf
%configure

%build
%make_build -j1

%install
%make_install

# fix doc path
mkdir -p %{buildroot}%{_defaultdocdir}/%{devname}
mv %{buildroot}%{_datadir}/html %{buildroot}%{_defaultdocdir}/%{devname}/html

