# son-sm


This repository contains Function- and Service-Specific Manager (FSM/SSM) base classes, helpers, examples, and utilities that are provided to support SSM/FSM development.

FSMs and SSMs are small programs or workflow definitions implemented by a network function/service developer with the help of SONATA’s SDK and shipped within the service package. Typical examples for such specific managers are custom service scaling and placement algorithms which place VNFs near to the users and automatically adapt the deployment to the current workload. Using these managers, the SONATA platform offers a novel level of flexibility to network function/service developers by adding programmability directly to the management and orchestration system. This goes beyond existing orchestration approaches where service management strategies are either limited to a predefined set of strategies or simple, customizable rules, e.g., for autoscaling. FSMs/SSMs, in contrast, can be complete programs that can consume information like monitoring data, do complex computations to optimise their decisions, and instruct other components of the system to act accordingly.

More details about SSMs and FSMs are available on the following link:

* [SONATA: Service Programming and Orchestration for Virtualized Software Networks](http://arxiv.org/abs/1605.05850)

### Cloning

The following command should be used to clone the son-sm repository:

`git clone --recursive https://github.com/sonata-nfv/son-sm.git`

### Contributing
Contributing to the son-sm is really easy. You must:

1. Clone [this repository](http://github.com/sonata-nfv/son-sm);
2. Work on your proposed changes, preferably through submiting [issues](https://github.com/sonata-nfv/son-sm/issues);
3. Submit a Pull Request;
4. Follow/answer related [issues](https://github.com/sonata-nfv/son-sm/issues) (see Feedback-Chanel, below).

## License

Son-sm is published under Apache 2.0 license. Please see the LICENSE file for more details.


---
#### Lead Developers

The following lead developers are responsible for this repository and have admin rights. They can, for example, merge pull requests.

* Hadi Razzaghi Kouchaksaraei (https://github.com/hadik3r)

#### Feedback-Chanel

* You may use the mailing list [sonata-dev@lists.atosresearch.eu](mailto:sonata-dev@lists.atosresearch.eu)
* [GitHub issues](https://github.com/sonata-nfv/son-sm/issues)
