#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'
require 'shared_types'


module Operation
  ADD = 1
  SUBTRACT = 2
  MULTIPLY = 3
  DIVIDE = 4
  VALUE_MAP = {1 => "ADD", 2 => "SUBTRACT", 3 => "MULTIPLY", 4 => "DIVIDE"}
  VALID_VALUES = Set.new([ADD, SUBTRACT, MULTIPLY, DIVIDE]).freeze
end

# Structs are the basic complex data structures. They are comprised of fields
# which each have an integer identifier, a type, a symbolic name, and an
# optional default value.
# 
# Fields can be declared "optional", which ensures they will not be included
# in the serialized output if they aren't set.  Note that this requires some
# manual management in some languages.
class Work
  include ::Thrift::Struct, ::Thrift::Struct_Union
  NUM1 = 1
  NUM2 = 2
  OP = 3
  COMMENT = 4

  FIELDS = {
    NUM1 => {:type => ::Thrift::Types::I32, :name => 'num1', :default => 0},
    NUM2 => {:type => ::Thrift::Types::I32, :name => 'num2'},
    OP => {:type => ::Thrift::Types::I32, :name => 'op', :enum_class => ::Operation},
    COMMENT => {:type => ::Thrift::Types::STRING, :name => 'comment', :optional => true}
  }

  def struct_fields; FIELDS; end

  def validate
    unless @op.nil? || ::Operation::VALID_VALUES.include?(@op)
      raise ::Thrift::ProtocolException.new(::Thrift::ProtocolException::UNKNOWN, 'Invalid value of field op!')
    end
  end

  ::Thrift::Struct.generate_accessors self
end

# Structs can also be exceptions, if they are nasty.
class InvalidOperation < ::Thrift::Exception
  include ::Thrift::Struct, ::Thrift::Struct_Union
  WHATOP = 1
  WHY = 2

  FIELDS = {
    WHATOP => {:type => ::Thrift::Types::I32, :name => 'whatOp'},
    WHY => {:type => ::Thrift::Types::STRING, :name => 'why'}
  }

  def struct_fields; FIELDS; end

  def validate
  end

  ::Thrift::Struct.generate_accessors self
end

