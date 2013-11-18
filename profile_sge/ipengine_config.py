# Configuration file for ipengine.

c = get_config()

#------------------------------------------------------------------------------
# IPEngineApp configuration
#------------------------------------------------------------------------------

# IPEngineApp will inherit config from: BaseParallelApplication,
# BaseIPythonApplication, Application

# The IPython profile to use.
# c.IPEngineApp.profile = u'default'

# Set the log level by value or name.
# c.IPEngineApp.log_level = 30

# specify a command to be run at startup
# c.IPEngineApp.startup_command = ''

# Set the working dir for the process.
# c.IPEngineApp.work_dir = u'/home/alexbw/.config/ipython'

# whether to log to a file
# c.IPEngineApp.log_to_file = False

# The URL for the iploggerapp instance, for forwarding logging to a central
# location.
# c.IPEngineApp.log_url = ''

# Whether to create profile dir if it doesn't exist
# c.IPEngineApp.auto_create = False

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPEngineApp.verbose_crash = False

# whether to cleanup old logfiles before starting
# c.IPEngineApp.clean_logs = False

# String id to add to runtime files, to prevent name collisions when using
# multiple clusters with a single profile simultaneously.
# 
# When set, files will be named like: 'ipcontroller-<cluster_id>-engine.json'
# 
# Since this is text inserted into filenames, typical recommendations apply:
# Simple character strings are ideal, and spaces are not recommended (but should
# generally work).
# c.IPEngineApp.cluster_id = ''

# specify a script to be run at startup
# c.IPEngineApp.startup_script = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPEngineApp.copy_config_files = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPEngineApp.ipython_dir = u'/home/alexbw/.config/ipython'

# The Logging format template
# c.IPEngineApp.log_format = '[%(name)s] %(message)s'

# 
# c.IPEngineApp.url_file_name = u'ipcontroller-engine.json'

# The full location of the file containing the connection information for the
# controller. If this is not given, the file must be in the security directory
# of the cluster directory.  This location is resolved using the `profile` or
# `profile_dir` options.
# c.IPEngineApp.url_file = u''

# Whether to overwrite existing config files when copying
# c.IPEngineApp.overwrite = False

# The maximum number of seconds to wait for url_file to exist. This is useful
# for batch-systems and shared-filesystems where the controller and engine are
# started at the same time and it may take a moment for the controller to write
# the connector files.
c.IPEngineApp.wait_for_url_file = 2400

#------------------------------------------------------------------------------
# ZMQInteractiveShell configuration
#------------------------------------------------------------------------------

# A subclass of InteractiveShell for ZMQ.

# ZMQInteractiveShell will inherit config from: InteractiveShell

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.ZMQInteractiveShell.color_info = True

# 
# c.ZMQInteractiveShell.history_length = 10000

# Don't call post-execute functions that have failed in the past.
# c.ZMQInteractiveShell.disable_failing_post_execute = False

# Show rewritten input, e.g. for autocall.
# c.ZMQInteractiveShell.show_rewritten_input = True

# Set the color scheme (NoColor, Linux, or LightBG).
# c.ZMQInteractiveShell.colors = 'Linux'

# 
# c.ZMQInteractiveShell.separate_in = '\n'

# Deprecated, use PromptManager.in2_template
# c.ZMQInteractiveShell.prompt_in2 = '   .\\D.: '

# 
# c.ZMQInteractiveShell.separate_out = ''

# Deprecated, use PromptManager.in_template
# c.ZMQInteractiveShell.prompt_in1 = 'In [\\#]: '

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
# normal reload(), but deep_reload will still be available as dreload().
# c.ZMQInteractiveShell.deep_reload = False

# Make IPython automatically call any callable object even if you didn't type
# explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
# The value can be '0' to disable the feature, '1' for 'smart' autocall, where
# it is not applied if there are no more arguments on the line, and '2' for
# 'full' autocall, where all callable objects are automatically called (even if
# no arguments are present).
# c.ZMQInteractiveShell.autocall = 0

# 
# c.ZMQInteractiveShell.separate_out2 = ''

# Deprecated, use PromptManager.justify
# c.ZMQInteractiveShell.prompts_pad_left = True

# 
# c.ZMQInteractiveShell.readline_parse_and_bind = ['tab: complete', '"\\C-l": clear-screen', 'set show-all-if-ambiguous on', '"\\C-o": tab-insert', '"\\C-r": reverse-search-history', '"\\C-s": forward-search-history', '"\\C-p": history-search-backward', '"\\C-n": history-search-forward', '"\\e[A": history-search-backward', '"\\e[B": history-search-forward', '"\\C-k": kill-line', '"\\C-u": unix-line-discard']

# Enable magic commands to be called without the leading %.
# c.ZMQInteractiveShell.automagic = True

# 
# c.ZMQInteractiveShell.debug = False

# 
# c.ZMQInteractiveShell.object_info_string_level = 0

# 
# c.ZMQInteractiveShell.ipython_dir = ''

# 
# c.ZMQInteractiveShell.readline_remove_delims = '-/~'

# Start logging to the default log file.
# c.ZMQInteractiveShell.logstart = False

# The name of the logfile to use.
# c.ZMQInteractiveShell.logfile = ''

# 
# c.ZMQInteractiveShell.wildcards_case_sensitive = True

# Save multi-line entries as one entry in readline history
# c.ZMQInteractiveShell.multiline_history = True

# Start logging to the given file in append mode.
# c.ZMQInteractiveShell.logappend = ''

# 
# c.ZMQInteractiveShell.xmode = 'Context'

# 
# c.ZMQInteractiveShell.quiet = False

# Deprecated, use PromptManager.out_template
# c.ZMQInteractiveShell.prompt_out = 'Out[\\#]: '

# Set the size of the output cache.  The default is 1000, you can change it
# permanently in your config file.  Setting it to 0 completely disables the
# caching system, and the minimum value accepted is 20 (if you provide a value
# less than 20, it is reset to 0 and a warning is issued).  This limit is
# defined because otherwise you'll spend more time re-flushing a too small cache
# than working
# c.ZMQInteractiveShell.cache_size = 1000

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
# c.ZMQInteractiveShell.ast_node_interactivity = 'last_expr'

# Automatically call the pdb debugger after every exception.
# c.ZMQInteractiveShell.pdb = False

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialiization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Username for the Session. Default is your system username.
# c.Session.username = 'alexbw'

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# The UUID identifying this session.
# c.Session.session = u''

# execution key, for extra authentication.
# c.Session.key = ''

# Debug output in the Session
# c.Session.debug = False

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# path to file containing execution key.
# c.Session.keyfile = ''

#------------------------------------------------------------------------------
# EngineFactory configuration
#------------------------------------------------------------------------------

# IPython engine

# EngineFactory will inherit config from: RegistrationFactory

# The SSH private key file to use when tunneling connections to the Controller.
# c.EngineFactory.sshkey = u''

# The 0MQ url used for registration. This sets transport, ip, and port in one
# variable. For example: url='tcp://127.0.0.1:12345' or url='epgm://*:90210'
# c.EngineFactory.url = ''

# The IP address for registration.  This is generally either '127.0.0.1' for
# loopback only or '*' for all interfaces. [default: '127.0.0.1']
# c.EngineFactory.ip = '127.0.0.1'

# The 0MQ transport for communications.  This will likely be the default of
# 'tcp', but other values include 'ipc', 'epgm', 'inproc'.
# c.EngineFactory.transport = 'tcp'

# The OutStream for handling stdout/err. Typically
# 'IPython.zmq.iostream.OutStream'
# c.EngineFactory.out_stream_factory = 'IPython.zmq.iostream.OutStream'

# The class for handling displayhook. Typically
# 'IPython.zmq.displayhook.ZMQDisplayHook'
# c.EngineFactory.display_hook_factory = 'IPython.zmq.displayhook.ZMQDisplayHook'

# The port on which the Hub listens for registration.
# c.EngineFactory.regport = 0

# Whether to use paramiko instead of openssh for tunnels.
# c.EngineFactory.paramiko = False

# The time (in seconds) to wait for the Controller to respond to registration
# requests before giving up.
c.EngineFactory.timeout = 2400

# The SSH server to use for tunneling connections to the Controller.
# c.EngineFactory.sshserver = u''

# The location (an IP address) of the controller.  This is used for
# disambiguating URLs, to determine whether loopback should be used to connect
# or the public address.
# c.EngineFactory.location = u''

#------------------------------------------------------------------------------
# Kernel configuration
#------------------------------------------------------------------------------

# 
# c.Kernel._execute_sleep = 0.0005

# 
# c.Kernel._poll_interval = 0.05

#------------------------------------------------------------------------------
# MPI configuration
#------------------------------------------------------------------------------

# Configurable for MPI initialization

# 
# c.MPI.default_inits = {'pytrilinos': 'from PyTrilinos import Epetra\nclass SimpleStruct:\npass\nmpi = SimpleStruct()\nmpi.rank = 0\nmpi.size = 0\n', 'mpi4py': 'from mpi4py import MPI as mpi\nmpi.size = mpi.COMM_WORLD.Get_size()\nmpi.rank = mpi.COMM_WORLD.Get_rank()\n'}

# Initialization code for MPI
# c.MPI.init_script = ''

# How to enable MPI (mpi4py, pytrilinos, or empty string to disable).
# c.MPI.use = ''
