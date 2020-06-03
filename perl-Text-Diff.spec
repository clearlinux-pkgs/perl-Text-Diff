#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Diff
Version  : 1.45
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-diff-perl/libtext-diff-perl_1.45-1.debian.tar.xz
Summary  : 'Perform diffs on files and record sets'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0 MIT
Requires: perl-Text-Diff-license = %{version}-%{release}
Requires: perl-Text-Diff-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)

%description
NAME
Text::Diff - Perform diffs on files and record sets
SYNOPSIS
use Text::Diff;

%package dev
Summary: dev components for the perl-Text-Diff package.
Group: Development
Provides: perl-Text-Diff-devel = %{version}-%{release}
Requires: perl-Text-Diff = %{version}-%{release}

%description dev
dev components for the perl-Text-Diff package.


%package license
Summary: license components for the perl-Text-Diff package.
Group: Default

%description license
license components for the perl-Text-Diff package.


%package perl
Summary: perl components for the perl-Text-Diff package.
Group: Default
Requires: perl-Text-Diff = %{version}-%{release}

%description perl
perl components for the perl-Text-Diff package.


%prep
%setup -q -n Text-Diff-1.45
cd %{_builddir}
tar xf %{_sourcedir}/libtext-diff-perl_1.45-1.debian.tar.xz
cd %{_builddir}/Text-Diff-1.45
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Diff-1.45/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Diff
cp %{_builddir}/Text-Diff-1.45/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Diff/740cb0ad7c45b0c0fe1fcaee03cffa1c3ce7f6e4
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Diff/c266b9f053cd302a9145154d1d86ae99a99cee8d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Diff.3
/usr/share/man/man3/Text::Diff::Config.3
/usr/share/man/man3/Text::Diff::Table.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Diff/740cb0ad7c45b0c0fe1fcaee03cffa1c3ce7f6e4
/usr/share/package-licenses/perl-Text-Diff/c266b9f053cd302a9145154d1d86ae99a99cee8d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Text/Diff.pm
/usr/lib/perl5/vendor_perl/5.30.3/Text/Diff/Config.pm
/usr/lib/perl5/vendor_perl/5.30.3/Text/Diff/Table.pm
