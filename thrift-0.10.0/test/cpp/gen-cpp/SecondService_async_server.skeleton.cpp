// This autogenerated skeleton file illustrates one way to adapt a synchronous
// interface into an asynchronous interface. You should copy it to another
// filename to avoid overwriting it and rewrite as asynchronous any functions
// that would otherwise introduce unwanted latency.

#include "SecondService.h"
#include <thrift/protocol/TBinaryProtocol.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::async;

using boost::shared_ptr;

using namespace  ::thrift::test;

class SecondServiceAsyncHandler : public SecondServiceCobSvIf {
 public:
  SecondServiceAsyncHandler() {
    syncHandler_ = std::auto_ptr<SecondServiceHandler>(new SecondServiceHandler);
    // Your initialization goes here
  }
  virtual ~SecondServiceAsyncHandler();

  void blahBlah(tcxx::function<void()> cob) {
    syncHandler_->blahBlah();
    return cob();
  }

  void secondtestString(tcxx::function<void(std::string const& _return)> cob, const std::string& thing) {
    std::string _return;
    syncHandler_->secondtestString(_return, thing);
    return cob(_return);
  }

 protected:
  std::auto_ptr<SecondServiceHandler> syncHandler_;
};

