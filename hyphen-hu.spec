Name: hyphen-hu
Summary: Hungarian hyphenation rules
%define upstreamid 20090612
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://download.github.com/nagybence-huhyphn-aa3fc85f5ea7450f84f0cd3881a09ca065198dfc.tar.gz
Group: Applications/Text
URL: http://www.tipogral.hu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
#BuildRequires: eruby, texlive
Requires: hyphen

%description
Hungarian hyphenation rules.

%prep
%setup -q -n nagybence-huhyphn-aa3fc85f5ea7450f84f0cd3881a09ca065198dfc
#disable for now as built-in patgen has too small a limit to rebuild
#ln -sf /usr/bin/patgen patgen
#touch words/*.txt

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hu.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hu_HR.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc gpl.txt README doc/huhyphn.pdf
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090612-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090612-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090612-2
- vanilla patgen's limit is too small

* Mon Jun 15 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090612-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081106-1
- latest version

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070907-1
- initial version
