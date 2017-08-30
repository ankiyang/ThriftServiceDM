/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef Inherited_H
#define Inherited_H

#include <thrift/TDispatchProcessor.h>
#include <thrift/async/TConcurrentClientSyncInfo.h>
#include "DebugProtoTest_types.h"
#include "Srv.h"

namespace thrift { namespace test { namespace debug {

#ifdef _WIN32
  #pragma warning( push )
  #pragma warning (disable : 4250 ) //inheriting methods via dominance 
#endif

class InheritedIf : virtual public SrvIf {
 public:
  virtual ~InheritedIf() {}
  virtual int32_t identity(const int32_t arg) = 0;
};

class InheritedIfFactory : virtual public SrvIfFactory {
 public:
  typedef InheritedIf Handler;

  virtual ~InheritedIfFactory() {}

  virtual InheritedIf* getHandler(const ::apache::thrift::TConnectionInfo& connInfo) = 0;
  virtual void releaseHandler(SrvIf* /* handler */) = 0;
};

class InheritedIfSingletonFactory : virtual public InheritedIfFactory {
 public:
  InheritedIfSingletonFactory(const boost::shared_ptr<InheritedIf>& iface) : iface_(iface) {}
  virtual ~InheritedIfSingletonFactory() {}

  virtual InheritedIf* getHandler(const ::apache::thrift::TConnectionInfo&) {
    return iface_.get();
  }
  virtual void releaseHandler(SrvIf* /* handler */) {}

 protected:
  boost::shared_ptr<InheritedIf> iface_;
};

class InheritedNull : virtual public InheritedIf , virtual public SrvNull {
 public:
  virtual ~InheritedNull() {}
  int32_t identity(const int32_t /* arg */) {
    int32_t _return = 0;
    return _return;
  }
};

typedef struct _Inherited_identity_args__isset {
  _Inherited_identity_args__isset() : arg(false) {}
  bool arg :1;
} _Inherited_identity_args__isset;

class Inherited_identity_args {
 public:

  Inherited_identity_args(const Inherited_identity_args&);
  Inherited_identity_args& operator=(const Inherited_identity_args&);
  Inherited_identity_args() : arg(0) {
  }

  virtual ~Inherited_identity_args() throw();
  int32_t arg;

  _Inherited_identity_args__isset __isset;

  void __set_arg(const int32_t val);

  bool operator == (const Inherited_identity_args & rhs) const
  {
    if (!(arg == rhs.arg))
      return false;
    return true;
  }
  bool operator != (const Inherited_identity_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Inherited_identity_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class Inherited_identity_pargs {
 public:


  virtual ~Inherited_identity_pargs() throw();
  const int32_t* arg;

  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _Inherited_identity_result__isset {
  _Inherited_identity_result__isset() : success(false) {}
  bool success :1;
} _Inherited_identity_result__isset;

class Inherited_identity_result {
 public:

  Inherited_identity_result(const Inherited_identity_result&);
  Inherited_identity_result& operator=(const Inherited_identity_result&);
  Inherited_identity_result() : success(0) {
  }

  virtual ~Inherited_identity_result() throw();
  int32_t success;

  _Inherited_identity_result__isset __isset;

  void __set_success(const int32_t val);

  bool operator == (const Inherited_identity_result & rhs) const
  {
    if (!(success == rhs.success))
      return false;
    return true;
  }
  bool operator != (const Inherited_identity_result &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Inherited_identity_result & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _Inherited_identity_presult__isset {
  _Inherited_identity_presult__isset() : success(false) {}
  bool success :1;
} _Inherited_identity_presult__isset;

class Inherited_identity_presult {
 public:


  virtual ~Inherited_identity_presult() throw();
  int32_t* success;

  _Inherited_identity_presult__isset __isset;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);

};

class InheritedClient : virtual public InheritedIf, public SrvClient {
 public:
  InheritedClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) :
    SrvClient(prot, prot) {}
  InheritedClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, boost::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) :    SrvClient(iprot, oprot) {}
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getInputProtocol() {
    return piprot_;
  }
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getOutputProtocol() {
    return poprot_;
  }
  int32_t identity(const int32_t arg);
  void send_identity(const int32_t arg);
  int32_t recv_identity();
};

class InheritedProcessor : public SrvProcessor {
 protected:
  boost::shared_ptr<InheritedIf> iface_;
  virtual bool dispatchCall(::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, const std::string& fname, int32_t seqid, void* callContext);
 private:
  typedef  void (InheritedProcessor::*ProcessFunction)(int32_t, ::apache::thrift::protocol::TProtocol*, ::apache::thrift::protocol::TProtocol*, void*);
  typedef std::map<std::string, ProcessFunction> ProcessMap;
  ProcessMap processMap_;
  void process_identity(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
 public:
  InheritedProcessor(boost::shared_ptr<InheritedIf> iface) :
    SrvProcessor(iface),
    iface_(iface) {
    processMap_["identity"] = &InheritedProcessor::process_identity;
  }

  virtual ~InheritedProcessor() {}
};

class InheritedProcessorFactory : public ::apache::thrift::TProcessorFactory {
 public:
  InheritedProcessorFactory(const ::boost::shared_ptr< InheritedIfFactory >& handlerFactory) :
      handlerFactory_(handlerFactory) {}

  ::boost::shared_ptr< ::apache::thrift::TProcessor > getProcessor(const ::apache::thrift::TConnectionInfo& connInfo);

 protected:
  ::boost::shared_ptr< InheritedIfFactory > handlerFactory_;
};

class InheritedMultiface : virtual public InheritedIf, public SrvMultiface {
 public:
  InheritedMultiface(std::vector<boost::shared_ptr<InheritedIf> >& ifaces) : ifaces_(ifaces) {
    std::vector<boost::shared_ptr<InheritedIf> >::iterator iter;
    for (iter = ifaces.begin(); iter != ifaces.end(); ++iter) {
      SrvMultiface::add(*iter);
    }
  }
  virtual ~InheritedMultiface() {}
 protected:
  std::vector<boost::shared_ptr<InheritedIf> > ifaces_;
  InheritedMultiface() {}
  void add(boost::shared_ptr<InheritedIf> iface) {
    SrvMultiface::add(iface);
    ifaces_.push_back(iface);
  }
 public:
  int32_t identity(const int32_t arg) {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->identity(arg);
    }
    return ifaces_[i]->identity(arg);
  }

};

// The 'concurrent' client is a thread safe client that correctly handles
// out of order responses.  It is slower than the regular client, so should
// only be used when you need to share a connection among multiple threads
class InheritedConcurrentClient : virtual public InheritedIf, public SrvConcurrentClient {
 public:
  InheritedConcurrentClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) :
    SrvConcurrentClient(prot, prot) {}
  InheritedConcurrentClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, boost::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) :    SrvConcurrentClient(iprot, oprot) {}
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getInputProtocol() {
    return piprot_;
  }
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getOutputProtocol() {
    return poprot_;
  }
  int32_t identity(const int32_t arg);
  int32_t send_identity(const int32_t arg);
  int32_t recv_identity(const int32_t seqid);
};

#ifdef _WIN32
  #pragma warning( pop )
#endif

}}} // namespace

#endif
