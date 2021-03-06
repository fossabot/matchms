################################################################################
matchms
################################################################################

.. list-table::
   :widths: 25 25
   :header-rows: 1

   * - fair-software.nl recommendations
     - Badges
   * - \1. Code repository
     - |GitHub Badge|
   * - \2. License
     - |License Badge| |FOSSA Badge|
   * - \3. Community Registry
     - |Conda Badge| |Research Software Directory Badge|
   * - \4. Enable Citation
     - |Zenodo Badge|
   * - \5. Checklist
     - |CII Best Practices Badge|
   * - **Other best practices**
     -
   * - Continuous integration
     - |GitHub Actions Badge|
   * - Documentation
     - |ReadTheDocs Badge|
   * - Code Quality
     - |Sonarcloud Quality Gate Badge| |Sonarcloud Coverage Badge|


(Customize these badges with your own links, and check https://shields.io/ or
https://badgen.net/ to see which other badges are available.)

.. |GitHub Badge| image:: https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue
   :target: https://github.com/matchms/matchms
   :alt: GitHub Badge

.. |License Badge| image:: https://img.shields.io/github/license/citation-file-format/cff-converter-python
   :target: https://github.com/matchms/matchms
   :alt: License Badge
.. |FOSSA Badge| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmatchms%2Fmatchms.svg?type=shield
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Fmatchms%2Fmatchms?ref=badge_shield
   :alt: FOSSA Badge

.. |Conda Badge| image:: https://anaconda.org/nlesc/matchms/badges/installer/conda.svg
   :target: https://conda.anaconda.org/nlesc
   :alt: Conda Badge
.. |Research Software Directory Badge| image:: https://img.shields.io/badge/rsd-matchms-00a3e3.svg
   :target: https://www.research-software.nl/software/matchms
   :alt: Research Software Directory Badge

.. |Zenodo Badge| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3716378.svg
   :target: https://doi.org/10.5281/zenodo.3716378
   :alt: Zenodo Badge

.. |CII Best Practices Badge| image:: https://bestpractices.coreinfrastructure.org/projects/3792/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/3792
   :alt: CII Best Practices Badge

.. |GitHub Actions Badge| image:: https://github.com/matchms/matchms/workflows/Build%20matchms/badge.svg
   :target: https://github.com/matchms/matchms/actions?query=workflow%3A%22Build+matchms%22
   :alt: GitHub Actions Badge

.. |ReadTheDocs Badge| image:: https://readthedocs.org/projects/matchms/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://matchms.readthedocs.io/en/latest/?badge=latest

.. |Sonarcloud Quality Gate Badge| image:: https://sonarcloud.io/api/project_badges/measure?project=matchms_matchms&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=matchms_matchms
   :alt: Sonarcloud Quality Gate

.. |Sonarcloud Coverage Badge| image:: https://sonarcloud.io/api/project_badges/measure?project=matchms_matchms&metric=coverage
   :target: https://sonarcloud.io/component_measures?id=matchms_matchms&metric=Coverage&view=list
   :alt: Sonarcloud Coverage

Vector representation and similarity measure for mass spectrometry data

The project setup is documented in `a separate document <project_setup.rst>`_.
Feel free to remove this document (and/or the link to this document) if you
don't need it.

***********************
Documentation for users
***********************

Installation
============

Install matchms from PyPI with

.. code-block:: console

  pip install --user matchms

Glossary of terms
=================

.. list-table::
   :header-rows: 1

   * - Term
     - Description
   * - adduct / addition product
     - During ionization in a mass spectrometer, the molecules of the injected compound break apart 
       into fragments. When fragments combine into a new compound, this is known as an addition 
       product, or adduct.  `Wikipedia <https://en.wikipedia.org/wiki/Adduct>`__
   * - GNPS
     - Knowledge base for sharing of mass spectrometry data (`link <https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp>`__).
   * - InChI / :code:`INCHI`
     - InChI is short for International Chemical Identifier. InChIs are useful
       in retrieving information associated with a certain molecule from a
       database.
   * - InChIKey / InChI key / :code:`INCHIKEY`
     - An indentifier for molecules. For example, the InChI key for carbon
       dioxide is :code:`InChIKey=CURLTUGMZLYLDI-UHFFFAOYSA-N` (yes, it
       includes the substring :code:`InChIKey=`).
   * - MGF File / Mascot Generic Format
     - A plan ASCII file format to store peak list data from a mass spectrometry experiment. Links: `matrixscience.com <http://www.matrixscience.com/help/data_file_help.html#GEN>`__, 
       `fiehnlab.ucdavis.edu <https://fiehnlab.ucdavis.edu/projects/lipidblast/mgf-files>`__.
   * - parent mass / :code:`parent_mass`
     - Actual mass (in Dalton) of the original compound prior to fragmentation. 
       It can be recalculated from the precursor m/z by taking      
       into account the charge state and proton/electron masses.
   * - precursor m/z / :code:`precursor_mz`
     - Mass-to-charge ratio of the compound targeted for fragmentation.
   * - SMILES
     - A line notation for describing the structure of chemical species using
       short ASCII strings. For example, water is encoded as :code:`O[H]O`,
       carbon dioxide is encoded as :code:`O=C=O`, etc. SMILES-encoded species may be converted to InChIKey `using a resolver like this one <https://cactus.nci.nih.gov/chemical/structure>`__. The Wikipedia entry for SMILES is `here <https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system>`__.


****************************
Documentation for developers
****************************

Installation
============

To install matchms, do:

.. code-block:: console

  git clone https://github.com/matchms/matchms.git
  cd matchms
  conda env create --name matchms --file=environment.yml
  conda activate matchms
  pip install .

Run tests (including coverage) with:

.. code-block:: console

  python setup.py test

Flowchart
=========

.. image:: flowchart.svg.png
  :width: 400
  :alt: Flowchart

Contributing
============

If you want to contribute to the development of matchms,
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

*****************************
Documentation for maintainers
*****************************


*******
License
*******

Copyright (c) 2020, Netherlands eScience Center

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



*******
Credits
*******

This package was created with `Cookiecutter
<https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template
<https://github.com/NLeSC/python-template>`_.
