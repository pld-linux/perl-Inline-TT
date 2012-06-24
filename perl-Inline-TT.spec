#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	TT
Summary:	Inline::TT Perl module
Summary(cs):	Modul Inline::TT pro Perl
Summary(da):	Perlmodul Inline::TT
Summary(de):	Inline::TT Perl Modul
Summary(es):	M�dulo de Perl Inline::TT
Summary(fr):	Module Perl Inline::TT
Summary(it):	Modulo di Perl Inline::TT
Summary(ja):	Inline::TT Perl �⥸�塼��
Summary(ko):	Inline::TT �� ����
Summary(nb):	Perlmodul Inline::TT
Summary(pl):	Modu� Perla Inline::TT
Summary(pt):	M�dulo de Perl Inline::TT
Summary(pt_BR):	M�dulo Perl Inline::TT
Summary(ru):	������ ��� Perl Inline::TT
Summary(sv):	Inline::TT Perlmodul
Summary(uk):	������ ��� Perl Inline::TT
Summary(zh_CN):	Inline::TT Perl ģ��
Name:		perl-Inline-TT
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	280dd7a08c533af56259dafb7770588c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Template-Toolkit >= 2.07
BuildRequires:	perl-Test-Simple >= 0.32
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::TT  - use TT BLOCK as Perl subs. Template-Toolkit is not just
a Templating Engine. It's a language. Inline::TT is a Inline plugin to
allow you to code your Perl subs in TT.

%description -l pl
Modu� Inline::TT - pozwalaj�cy na u�ywanie blok�w TT jako procedur
Perla. Template-Toolkit to nie tylko mechanizm obs�uguj�cy wzorce - to
j�zyk. A Inline::TT pozwala na pisanie procedur Perla w j�zyku TT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/TT.pm
%{_mandir}/man3/*
