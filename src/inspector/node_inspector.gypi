{
  'variables': {
    'protocol_tool_path': '../../deps/v8/third_party/inspector_protocol',
    'node_inspector_generated_path': '<(SHARED_INTERMEDIATE_DIR)/node_inspector',
    'node_inspector_generated_sources': [
      '<(node_inspector_generated_path)/protocol/Forward.h',
      '<(node_inspector_generated_path)/protocol/Protocol.cpp',
      '<(node_inspector_generated_path)/protocol/Protocol.h',
      '<(node_inspector_generated_path)/protocol/NodeWorker.cpp',
      '<(node_inspector_generated_path)/protocol/NodeWorker.h',
      '<(node_inspector_generated_path)/protocol/NodeTracing.cpp',
      '<(node_inspector_generated_path)/protocol/NodeTracing.h',
    ],
  },
  'defines': [
    'HAVE_INSPECTOR=1',
  ],
  'sources': [
    '../inspector_agent.cc',
    '../inspector_io.cc',
    '../inspector_agent.h',
    '../inspector_io.h',
    '../inspector_js_api.cc',
    '../inspector_socket.cc',
    '../inspector_socket.h',
    '../inspector_socket_server.cc',
    '../inspector_socket_server.h',
    'main_thread_interface.cc',
    'main_thread_interface.h',
    'node_string.cc',
    'node_string.h',
    'tracing_agent.cc',
    'tracing_agent.h',
    'worker_agent.cc',
    'worker_agent.h',
    'worker_inspector.cc',
    'worker_inspector.h',
    'node_protocol/Forward.h',
    'node_protocol/Protocol.cpp',
    'node_protocol/Protocol.h',
    'node_protocol/NodeWorker.cpp',
    'node_protocol/NodeWorker.h',
    'node_protocol/NodeTracing.cpp',
    'node_protocol/NodeTracing.h',

  ],
  'include_dirs': [
    '<(node_inspector_generated_path)',
  ],
  'copies': [
    {
      'files': [
        'node_protocol_config.json',
        'node_protocol.pdl',
      ],
      'destination': '<(node_inspector_generated_path)',
    }
  ],
  'actions': [
    {
      'action_name': 'concatenate_protocols',
      'inputs': [
        '../../deps/v8/src/inspector/js_protocol.json',
        '<(node_inspector_generated_path)/node_protocol.json',
      ],
      'outputs': [
        '<(node_inspector_generated_path)/concatenated_protocol.json',
      ],
      'action': [
        'python',
        'tools/inspector_protocol/ConcatenateProtocols.py',
        '<@(_inputs)',
        '<@(_outputs)',
      ],
    },
    {
      'action_name': 'v8_inspector_compress_protocol_json',
      'process_outputs_as_sources': 0,
      'inputs': [
        '<(node_inspector_generated_path)/concatenated_protocol.json',
      ],
      'outputs': [
        '<(node_inspector_generated_path)/concatenated_protocol/v8_inspector_protocol_json.h',
      ],
      'action': [
        'python',
        'tools/compress_json.py',
        '<@(_inputs)',
        '<@(_outputs)',
      ],
    },
  ],
}
