#ifndef FWCore_Framework_InputTagMatch_h
#define FWCore_Framework_InputTagMatch_h

/** \class edm::InputTagMatch

This is intended to be used with the class GetterOfProducts.
See comments in the file GetterOfProducts.h for a description.

\author V. Adler

*/

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Provenance/interface/ProductDescription.h"

#include <string>

namespace edm {

  class InputTagMatch {
  public:
    InputTagMatch(edm::InputTag const& inputTag) : inputTag_(inputTag) {}

    bool operator()(edm::ProductDescription const& productDescription) {
      bool result(true);
      bool match(false);
      if (!inputTag_.label().empty()) {
        match = true;
        result = (result && productDescription.moduleLabel() == inputTag_.label());
      }
      if (!inputTag_.instance().empty()) {
        match = true;
        result = (result && productDescription.productInstanceName() == inputTag_.instance());
      }
      if (!inputTag_.process().empty()) {
        match = true;
        result = (result && productDescription.processName() == inputTag_.process());
      }
      if (match)
        return result;
      return false;
    }

  private:
    edm::InputTag inputTag_;
  };
}  // namespace edm
#endif
