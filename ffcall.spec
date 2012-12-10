%define	name	ffcall
%define libname_orig    lib%{name}

%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		%{name}
Version:	1.10
Release:	9
License:	GPLv2
Group:		Development/C
URL:		ftp://ftp.santafe.edu/pub/gnu/
Source:		ftp://ftp.santafe.edu/pub/gnu/%{name}-%{version}.tar.bz2
Patch0:		ffcall-make-jN.patch

%package 	-n %{libname}
Summary:        Libraries that can be used to build foreign function call interfaces
Group:          Development/Other
Provides:	%{libname_orig} = %{version}-%{release}
Conflicts:      %mklibname %{name} 0 -d

%package        -n %{libnamedev}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:          Development/Other
Requires:	%{libname} = %{version}
Provides:	%{libname_orig}-devel 
Provides:	%{name}-devel
Obsoletes:	%mklibname %{name} 0 -d

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
    (a reentrant combination of vacall and trampoline)

    This version B includes some minor configuration changes so that files
    are installed in the proper place. Also it compiles on cygwin and mingw32.

%description -n %{libname}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
    (a reentrant combination of vacall and trampoline)

    This version B includes some minor configuration changes so that files
    are installed in the proper place. Also it compiles on cygwin and mingw32.


%description -n %{libnamedev}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x --enable-shared
%make

%install
# make install does not create all necessary directories
mkdir -p %buildroot %buildroot/%_includedir %buildroot/%_libdir %buildroot/%_mandir
%makeinstall_std

mkdir -p %{buildroot}%{_defaultdocdir}/%{libnamedev}
mv %{buildroot}/usr/share/html %{buildroot}%{_defaultdocdir}/%{libnamedev}/html

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc NEWS README PLATFORMS
%_includedir/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*


%changelog
* Sat Sep 18 2010 Funda Wang <fwang@mandriva.org> 1.10-8mdv2011.0
+ Revision: 579336
- add missing requires

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 1.10-7mdv2011.0
+ Revision: 572780
- add patch to build in parallel

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.10-6mdv2010.0
+ Revision: 428718
- rebuild

* Fri Jul 18 2008 Funda Wang <fwang@mandriva.org> 1.10-5mdv2009.0
+ Revision: 238018
- Build with -fPIC

* Fri Jul 11 2008 Funda Wang <fwang@mandriva.org> 1.10-4mdv2009.0
+ Revision: 233843
- should be obsoletes rather than conflicts

* Fri Jul 11 2008 Funda Wang <fwang@mandriva.org> 1.10-3mdv2009.0
+ Revision: 233827
- use configure2_5x

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 12 2008 Frederik Himpe <fhimpe@mandriva.org> 1.10-3mdv2008.1
+ Revision: 166454
- Fix summary
- Clean buildroot
- Fix devel package provides
- Remove shared libraries from -devel package and put them in lib package
- Adapt devel package name to new policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Mon Apr 02 2007 Pascal Terjan <pterjan@mandriva.org> 1.10-2mdv2007.1
+ Revision: 150177
- Use the macros, this avoids a lot of hacks and fixes build on x86_64
- Use mkrel
- Use autoconf2.5
- Fix group
- Don't have 2 dirs for the doc
- Import ffcall

* Sat Jun 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.10-1mdk
- 1.10

* Sat May 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.9-1mdk
- 1.9

