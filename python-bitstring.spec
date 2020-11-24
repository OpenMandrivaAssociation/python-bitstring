%global srcname bitstring

Name:           python-%{srcname}
Version:        3.1.7
Release:        3%{?dist}
Summary:        Simple construction, analysis and modification of binary data

License:        MIT
URL:            https://github.com/scott-griffiths/%{srcname}
Source0:        https://github.com/scott-griffiths/%{srcname}/archive/%{srcname}-%{version}/%{srcname}-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

%description
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.

%prep
%autosetup -n %{srcname}-%{srcname}-%{version}

dos2unix README.rst release_notes.txt
sed -i '1{s|^#!/usr/bin/env python||}' %{srcname}.py


%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst release_notes.txt
%{python_sitelib}/%{srcname}.py
%{python_sitelib}/__pycache__/%{srcname}*
%{python_sitelib}/%{srcname}-%{version}-py*.egg-info
