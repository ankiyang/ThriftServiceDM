#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'
require 'thrift_namespaced_spec_types'

module NamespacedSpecNamespace
  module NamespacedNonblockingService
    class Client
      include ::Thrift::Client

      def greeting(english)
        send_greeting(english)
        return recv_greeting()
      end

      def send_greeting(english)
        send_message('greeting', Greeting_args, :english => english)
      end

      def recv_greeting()
        result = receive_message(Greeting_result)
        return result.success unless result.success.nil?
        raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'greeting failed: unknown result')
      end

      def block()
        send_block()
        return recv_block()
      end

      def send_block()
        send_message('block', Block_args)
      end

      def recv_block()
        result = receive_message(Block_result)
        return result.success unless result.success.nil?
        raise ::Thrift::ApplicationException.new(::Thrift::ApplicationException::MISSING_RESULT, 'block failed: unknown result')
      end

      def unblock(n)
        send_unblock(n)
      end

      def send_unblock(n)
        send_oneway_message('unblock', Unblock_args, :n => n)
      end
      def shutdown()
        send_shutdown()
      end

      def send_shutdown()
        send_oneway_message('shutdown', Shutdown_args)
      end
      def sleep(seconds)
        send_sleep(seconds)
        recv_sleep()
      end

      def send_sleep(seconds)
        send_message('sleep', Sleep_args, :seconds => seconds)
      end

      def recv_sleep()
        result = receive_message(Sleep_result)
        return
      end

    end

    class Processor
      include ::Thrift::Processor

      def process_greeting(seqid, iprot, oprot)
        args = read_args(iprot, Greeting_args)
        result = Greeting_result.new()
        result.success = @handler.greeting(args.english)
        write_result(result, oprot, 'greeting', seqid)
      end

      def process_block(seqid, iprot, oprot)
        args = read_args(iprot, Block_args)
        result = Block_result.new()
        result.success = @handler.block()
        write_result(result, oprot, 'block', seqid)
      end

      def process_unblock(seqid, iprot, oprot)
        args = read_args(iprot, Unblock_args)
        @handler.unblock(args.n)
        return
      end

      def process_shutdown(seqid, iprot, oprot)
        args = read_args(iprot, Shutdown_args)
        @handler.shutdown()
        return
      end

      def process_sleep(seqid, iprot, oprot)
        args = read_args(iprot, Sleep_args)
        result = Sleep_result.new()
        @handler.sleep(args.seconds)
        write_result(result, oprot, 'sleep', seqid)
      end

    end

    # HELPER FUNCTIONS AND STRUCTURES

    class Greeting_args
      include ::Thrift::Struct, ::Thrift::Struct_Union
      ENGLISH = 1

      FIELDS = {
        ENGLISH => {:type => ::Thrift::Types::BOOL, :name => 'english'}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Greeting_result
      include ::Thrift::Struct, ::Thrift::Struct_Union
      SUCCESS = 0

      FIELDS = {
        SUCCESS => {:type => ::Thrift::Types::STRUCT, :name => 'success', :class => ::NamespacedSpecNamespace::Hello}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Block_args
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Block_result
      include ::Thrift::Struct, ::Thrift::Struct_Union
      SUCCESS = 0

      FIELDS = {
        SUCCESS => {:type => ::Thrift::Types::BOOL, :name => 'success'}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Unblock_args
      include ::Thrift::Struct, ::Thrift::Struct_Union
      N = 1

      FIELDS = {
        N => {:type => ::Thrift::Types::I32, :name => 'n'}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Unblock_result
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Shutdown_args
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Shutdown_result
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Sleep_args
      include ::Thrift::Struct, ::Thrift::Struct_Union
      SECONDS = 1

      FIELDS = {
        SECONDS => {:type => ::Thrift::Types::DOUBLE, :name => 'seconds'}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Sleep_result
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

  end

end
