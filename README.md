# gem_eyes
Little python3 script to search for security vulnerabilities and out-dated dependencies in rubygems


## Instalation
```
pip install requests
```
## Usage
```
python3 gem_eyes.py --file Gemfile
https://www.versioneye.com/ruby/nokogiri/1.6.1
Security Vulnerabilities:
 > Nokogiri Gem for JRuby XML Document Root Element Handling Memory ConsumptionRemote DoS
 > Nokogiri gem contains several vulnerabilities in libxml2 and libxslt
 > Nokogiri gem contains several vulnerabilities in libxml2
 > Nokogiri gem contains a heap-based buffer overflow vulnerability in libxml2
 > Denial of service or RCE from libxml2 and libxslt
 > Nokogiri gem contains several vulnerabilities in libxml2 and libxslt
 > Nokogiri gem contains two upstream vulnerabilities in libxslt 1.1.29
 > Security Notes
 > Nokogiri gem, via libxml, is affected by DoS and RCE vulnerabilities
Reference: https://www.versioneye.com/ruby/nokogiri/1.6.1
```
