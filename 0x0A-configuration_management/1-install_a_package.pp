# Install puppet-lint 2.5.0 package
package { 'puppet-lint':
  ensure   => '2.5.0',
  source   => 'http://rubygems.org/gems/',
  provider => 'gem',
}
