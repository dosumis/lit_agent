I have gathered extensive information about single-cell transcriptomics datasets available for astrocytes. Let me compile this comprehensive resource for you.

## Comprehensive Single Cell Transcriptomics Datasets for Astrocytes

### Mouse Brain - Regional Astrocyte Diversity

**Batiuk et al. 2020 - Mouse Cortex and Hippocampus**[1]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cortex and hippocampus (adult P56)
- **Method:** Smart-seq2 scRNA-seq
- **Cell numbers:** ~2,000 astrocytes (5 distinct subtypes identified)
- **Multimodal:** No (transcriptomics only)
- **GEO Accession:** GSE114000
- **Download links:**
  - Count matrix: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE114nnn/GSE114000/suppl/GSE114000_Counts_Batiuk_Martirosyan_Supplementary_Data3.tsv.gz
  - Metadata: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE114nnn/GSE114000/suppl/GSE114000_Metadata_Batiuk_Martirosyan_Supplementary_Data1.xlsx
- **Interactive database:** https://holt-sc.glialab.org/

**Bayraktar et al. 2020 - Cortical Astrocyte Layers**[2][3]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cerebral cortex (layered astrocyte populations)
- **Method:** scRNA-seq with LaST (Large-area Spatial Transcriptomic) map
- **Multimodal:** Yes (single-cell transcriptomics + spatial in situ hybridization)
- **GEO Accession:** GSE140822
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140822
- **Notes:** Identifies superficial, mid, and deep astrocyte layer identities with gradient patterns distinct from neuronal layers

**Endo et al. 2022 - Whole CNS Astrocyte Atlas**[4][5]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Comprehensive coverage across entire CNS (brain and spinal cord)
- **Method:** snRNA-seq
- **Cell numbers:** Large-scale (specific numbers in publication)
- **Multimodal:** Yes (transcriptomics linked to morphology measurements)
- **GEO Accession:** GSE198032 (includes subseries GSE198024 and GSE198027)
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198032
- **Notes:** Identifies gene networks correlated with astrocyte morphology; includes Alzheimer's disease risk genes

### Allen Brain Cell Atlas - Whole Mouse Brain[6][7][8]

**Yao et al. 2023 - Comprehensive Mouse Brain Atlas**
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Entire adult mouse brain (all regions)
- **Method:** 10x Chromium scRNA-seq (v2 and v3) + MERFISH spatial transcriptomics
- **Cell numbers:** ~7 million single-cell transcriptomes profiled; ~4.3 million QC-qualified cells; ~4.3 million MERFISH cells
- **Multimodal:** Yes (scRNA-seq + spatial transcriptomics + MERFISH)
- **Astrocyte classification:** Included in hierarchical taxonomy (34 classes, 338 subclasses, 1,201 supertypes, 5,322 clusters total; astrocytes comprise "Astrocyte" supercluster)
- **GEO Accession:** GSE246717
- **Download options:**
  - AWS S3 bucket: arn:aws:s3:::allen-brain-cell-atlas (no login required)
  - Data access tools: https://alleninstitute.github.io/abc_atlas_access/
  - Interactive portal: https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas
- **Data packages:** Expression matrices subdivided by anatomical region for efficient download
- **File formats:** AnnData (.h5ad), with AbcProjectCache Python package for data management

### Human Brain Astrocytes

**Human Brain Cell Atlas v1.0**[9]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Entire adult human brain (100+ dissections across forebrain, midbrain, hindbrain)
- **Method:** snRNA-seq
- **Cell numbers:** >3 million nuclei from 3 postmortem donors
- **Multimodal:** No (transcriptomics only)
- **Astrocyte identification:** Included in non-neuronal cell partition (888,300 non-neuronal cells total)
- **Access:** CELLxGENE portal
- **Download:** https://data.humancellatlas.org/hca-bio-networks/nervous-system/atlases/brain-v1-0
- **Notes:** 30 superclusters, 461 clusters, 3,313 subclusters; includes oligodendrocyte supercluster with astrocyte subpopulations

**Qian et al. 2023 - Large-Scale Human Brain Integration**[10][11]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Multiple brain regions across diseases
- **Method:** Integrated scRNA-seq from 302 publicly available datasets
- **Cell numbers:** Nearly 1 million cells
- **Multimodal:** Yes (scRNA-seq + spatial transcriptomics + proteomics)
- **Disease coverage:** Alzheimer's disease, Parkinson's disease, Huntington's disease, multiple sclerosis, epilepsy, chronic traumatic encephalopathy
- **Download:** Data available from GEO accessions of individual component studies
- **Notes:** Identifies 7 transcriptomic modules including M2 ECM and M4 stress modules; includes spatial transcriptomics validation in mouse

**Zhang & Sloan et al. 2016 - Human Fetal and Adult Astrocytes**[12][13]
- **Species:** Human (*Homo sapiens*) and Mouse (*Mus musculus*)
- **Regions:** Fetal and adult human cortex
- **Method:** Bulk RNA-seq of immunopanned astrocytes
- **GEO Accession:** GSE73721
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE73721
- **Multimodal:** No (transcriptomics only)
- **Notes:** Includes comparison with mouse astrocytes; demonstrates morphological differences between human and rodent astrocytes

**Serrano-Pozo et al. 2024 - Alzheimer's Disease Spatiotemporal**[14]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Five brain regions (entorhinal cortex, middle temporal gyrus, angular gyrus, primary visual cortex, precuneus)
- **Method:** snRNA-seq
- **Cell numbers:** 628,943 astrocyte nuclei from AD patients and controls
- **Multimodal:** No (transcriptomics only)
- **Download:** Data available via GEO (accession in publication)
- **Notes:** Maps astrocyte transcriptomic changes along AD progression; includes regional heterogeneity analysis

### Astrocyte Differentiation and Development

**Frazel et al. 2023 - Mouse and Human Astrocyte Differentiation**[15][16][17][18][19]
- **Species:** Mouse (*Mus musculus*) and Human (*Homo sapiens*)
- **Method:** scRNA-seq/snRNA-seq + snATAC-seq (multimodal dual sequencing)
- **Cell numbers:** ~298,000 cells and nuclei total (~113,000 from mouse across 15 timepoints; ~185,000 from human across multiple lines)
- **Timepoints:** Mouse differentiation from embryonic stem cells (15 stages); human from iPSCs (multiple stages)
- **Multimodal:** Yes (scRNA-seq/snRNA-seq + snATAC-seq for chromatin accessibility)
- **GEO Accession:** Available (check Nature Neuroscience 2023 paper supplementary)
- **Download:** Data in GEO and potentially GitHub
- **Notes:** Optimizes rapid astrocyte differentiation protocols; identifies fate specification genes; maps genomic regulatory regions

**Nfib/Sox9-induced Astrocyte Differentiation**[20][21]
- **Species:** Human (*Homo sapiens*)
- **Method:** scRNA-seq
- **Cell numbers:** >5,600 cells across timepoints
- **Timepoints:** Days 0, 1, 3, 8, 14, 21 during differentiation from iPSCs
- **Multimodal:** No (transcriptomics only)
- **Download:** Data available in Scientific Data 2024 publication
- **Notes:** Monoclonal and multi-line iPSC differentiation; establishes comprehensive astrocyte differentiation trajectories

### Cerebellar Astrocytes

**Cerrato Lab - Cerebellar Astrocyte Development**[22][23][24]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cerebellum (including Bergmann glia)
- **Method:** sc/snRNA-seq across postnatal developmental stages
- **Multimodal:** Yes (integrated with spatial transcriptomics)
- **Download:** BioRxiv preprint 2025 (data expected in GEO)
- **Notes:** Identifies multiple astrocyte subtypes including Bergmann glia subpopulations; maps developmental trajectories from radial glia

**Kwon et al. 2024 - Postnatal Cerebellar Development**[25]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cerebellum
- **Method:** Bulk RNA-seq of FACS-sorted astrocytes (Aldh1l1-GFP)
- **Timepoints:** P1, P7, P14, P28
- **Multimodal:** No (transcriptomics only)
- **Download:** Data available in publication
- **Notes:** Stage-specific astrocytic gene expression signatures during cerebellar development

**Kozareva & Martin et al. - Mouse Cerebellar Atlas**[26]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cerebellar cortex (all lobules)
- **Method:** High-throughput scRNA-seq
- **Cell numbers:** Large-scale comprehensive atlas
- **Multimodal:** Yes (transcriptomics linked to electrophysiology and morphology)
- **Access:** https://singlecell.broadinstitute.org/single_cell/study/SCP795
- **Notes:** Includes all cerebellar cell types; astrocytes and Bergmann glia characterized

### Spinal Cord Astrocytes

**Zhang et al. 2024 - Human Spinal Cord Atlas**[27]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Lumbar spinal cord enlargement
- **Method:** snRNA-seq + Visium spatial transcriptomics
- **Cell numbers:** 64,021 nuclei from 9 adult donors (6 male, 3 female, ages 35-59)
- **Multimodal:** Yes (snRNA-seq + spatial transcriptomics)
- **Astrocyte proportion:** 5.2% of total nuclei
- **Download:** Check eLife 2024 publication for data access
- **Notes:** Astrocytes distributed across gray and white matter; spatial mapping validated by immunofluorescence

**Milich et al. 2021 - Spinal Cord Injury**[28]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Thoracic spinal cord
- **Method:** scRNA-seq
- **Timepoints:** Uninjured, 1, 3, and 7 days post-injury
- **Cell numbers:** Comprehensive dataset of all cell types
- **Multimodal:** No (transcriptomics only)
- **Download:** Data available via journal (Journal of Experimental Medicine 2021)
- **Notes:** Characterizes injury-induced astrocyte subpopulations; identifies transient states during acute SCI

**Spinal Cord Injury - Multiple Studies**[29][30][31]
- **Species:** Mouse (*Mus musculus*)
- **Method:** scRNA-seq of GFAP+ lineage cells
- **GEO Accessions:** 
  - GSE202627 (sub-chronic SCI, GFAP lineage cells)
  - GSE189070 (acute to intermediate stages)
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202627
- **Multimodal:** No (transcriptomics only)
- **Notes:** Identifies astrocyte progenitor heterogeneity; tracks subpopulation dynamics across injury stages

### Hypothalamus - Astrocytes and Tanycytes

**Chen et al. 2017 - Hypothalamic Cell Diversity**[32][33][34]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Hypothalamus
- **Method:** Drop-seq
- **Cell numbers:** ~20,000 cells (11 non-neuronal and 34 neuronal clusters)
- **GEO Accession:** GSE87544
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87544
- **Multimodal:** No (transcriptomics only)
- **Notes:** Identifies tanycyte-specific markers; includes astrocyte and tanycyte populations; food deprivation perturbation experiment

**Campbell et al. - Arcuate Hypothalamus and Median Eminence**[35]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Arcuate nucleus-median eminence complex
- **Method:** Drop-seq
- **Cell numbers:** 20,921 cells (50 distinct populations)
- **GEO Accession:** GSE93374
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE93374
- **Interactive portal:** https://portals.broadinstitute.org/single_cell/study/a-molecular-census-of-arcuate-hypothalamus-and-median-eminence-cell-types
- **Multimodal:** No (transcriptomics only)
- **Notes:** Identifies rare tanycyte population at Arc-ME diffusion barrier; includes energy status perturbations

**Harkany et al. 2024 - Spatially Stratified Hypothalamic Astrocytes**[36]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Hypothalamus (multiple nuclei)
- **Method:** Integrated scRNA-seq from multiple datasets
- **Multimodal:** Yes (integrated with spatial transcriptomics)
- **Download:** Check Nature Neuroscience 2024 publication
- **Notes:** Reveals region-specific astrocyte heterogeneity across hypothalamic nuclei; identifies astrocyte subtypes supporting distinct neurocircuits

**Bai et al. 2024 - Human Embryonic Tanycytes**[37]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Hypothalamus (developmental)
- **Method:** scRNA-seq
- **Multimodal:** No (transcriptomics only)
- **Download:** Scientific Reports 2024
- **Notes:** Characterizes human tanycyte subtypes (α1, α2, β1, β2); maps developmental trajectories from radial glia

### Striatum Astrocytes

**Yu et al. 2020 - Context-Specific Striatal Astrocytes**[38]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Striatum
- **Method:** scRNA-seq + astrocyte-specific RNA-seq (RiboTag)
- **Cell numbers:** 20,912 striatal cells (n=3 mice)
- **Multimodal:** Yes (scRNA-seq + targeted astrocyte profiling)
- **Download:** Data available in Nature Communications 2020
- **Notes:** 11 transcriptomic clusters; assesses astrocyte responses to environmental perturbations; Huntington's disease analysis

**Single Factor Reprogramming in Striatum**[39]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Striatum
- **Method:** scRNA-seq of tdTomato+ cells (Aldh1l1-CreERT2 lineage)
- **Cell numbers:** 5,756 cells (Lenti-DLX2) + 4,610 cells (Lenti-GFP control)
- **GEO Accession:** Check PNAS 2022 publication
- **Multimodal:** No (transcriptomics only)
- **Notes:** Tracks astrocyte reprogramming trajectories; identifies astrocyte, NPC, neuroblast, and other populations

### Retina - Müller Glia and Astrocytes

**Menon et al. 2019 - Human Retina**[40]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Retina
- **Method:** Drop-seq and Seq-Well scRNA-seq
- **Cell numbers:** Thousands of cells across platforms
- **Multimodal:** No (transcriptomics only)
- **Download:** Check Nature Communications 2019 for data access
- **Notes:** Identifies Müller glia and astrocyte subpopulations; distinguishes glial markers; AMD genetic risk analysis

**Liu et al. 2022 - Müller Cell Diversity in AMD**[41]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Retina (macular)
- **Method:** scRNA-seq
- **Cell numbers:** 22,597 cells (4 AMD cases + 7 healthy controls)
- **Multimodal:** No (transcriptomics only)
- **Download:** Data from integrated published databases
- **Notes:** Reveals Müller cell heterogeneity; mtDNA expression divergence in disease

**Wei et al. 2023 - Light/Dark Adaptation**[42]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Retina
- **Method:** 10x Genomics scRNA-seq
- **Cell numbers:** 25,176 retinal cells (14,909 light-adapted + 10,267 dark-adapted)
- **Multimodal:** No (transcriptomics only)
- **Download:** Check Protein & Cell 2023 publication
- **Notes:** Characterizes Müller glia responses to light/dark adaptation; cell-cell communication analysis

**Yao et al. 2024 - OIR Model Multiomics**[43]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Retina (oxygen-induced retinopathy model)
- **Method:** Joint snRNA-seq + snATAC-seq
- **Cell numbers:** 6,347 cells
- **Multimodal:** Yes (transcriptomics + chromatin accessibility)
- **Download:** Check Scientific Reports 2024
- **Notes:** Müller cells/astrocytes show significant associations with proliferative diabetic retinopathy

### Reactive and Disease-Associated Astrocytes

**ssREAD Database - Alzheimer's Disease**[44][45][46][47][48][49][50]
- **Species:** Human (*Homo sapiens*) and Mouse (*Mus musculus*)
- **Coverage:** 277 sc/snRNA-seq datasets (67 studies, 7.3 million cells) + 381 spatial transcriptomics datasets (18 studies)
- **Method:** Integrated scRNA-seq, snRNA-seq, and spatial transcriptomics
- **Diseases:** Alzheimer's disease, control brain studies
- **Web portal:** https://bmblx.bmi.osumc.edu/ssread/
- **Download:** Available in multiple formats (.h5ad, .h5seurat) for Seurat and Scanpy
- **Multimodal:** Yes (scRNA-seq + spatial transcriptomics + spot deconvolution)
- **Notes:** Comprehensive AD database with cell clustering, DEG analysis, spatially variable genes, and regulatory network inference

**Scott et al. 2024 - Stroke Spatial Transcriptomics**[51][52]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cortex (stroke model)
- **Method:** 10x Chromium scRNA-seq + Visium spatial transcriptomics + tDISCO (spatially resolved single-cell omics)
- **Multimodal:** Yes (scRNA-seq + spatial transcriptomics + spatially resolved proteomics)
- **Download:** Check Nature Communications 2024
- **Notes:** Identifies proximal and distal astrocyte populations relative to stroke lesion; tDISCO provides spatial single-cell resolution for both transcriptomics and proteomics

**Leng et al. 2021 - Reactive Astrocytes in iPSC Models**[53][54]
- **Species:** Human (*Homo sapiens*)
- **Method:** scRNA-seq with CRISPRi screening
- **Cell source:** hiPSC-derived astrocytes
- **GEO Accession:** GSE182307
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182307
- **Multimodal:** Yes (scRNA-seq + CROP-seq with genetic perturbations)
- **Notes:** Systematically interrogates inflammatory reactivity pathways; identifies IL-6 and interferon signaling states

**Hasel et al. 2021 - Neuroinflammatory Astrocyte Subtypes**[55]
- **Species:** Mouse (*Mus musculus*)
- **Method:** scRNA-seq
- **Multimodal:** No (transcriptomics only)
- **Download:** Data in Nature Neuroscience 2021 publication
- **Notes:** Identifies region-specific inflammatory transitions; discovers super-responder astrocyte populations in strategic brain locations

### Multimodal: Patch-seq (Transcriptomics + Electrophysiology + Morphology)

**Allen Institute Patch-seq Resources**[56][57][58][59][60][61][62][63][64][65][66]
- **Species:** Mouse (*Mus musculus*), Human (*Homo sapiens*), Macaque (*Macaca mulatta*)
- **Method:** Patch-seq (whole-cell electrophysiology + morphology + Smart-seq2 transcriptomics)
- **Cell numbers:** 1,300+ neurons characterized for mouse motor cortex
- **Multimodal:** Yes (electrophysiology + morphology + transcriptomics - triple modality)
- **Web portal:** 
  - Morpho-Electric database: http://celltypes.brain-map.org/
  - Single-cell RNA-seq: https://portal.brain-map.org/atlases-and-data/rnaseq
- **GitHub:** https://github.com/AllenInstitute/patchseqtools
- **Protocol:** https://www.protocols.io/view/patch-seq-recording-and-extraction-detailed-protoc-bw6gphbw
- **Notes:** While primarily focused on neurons, methodology applicable to astrocytes; includes quality control tools and cell typing algorithms

**Note on Patch-seq for Astrocytes**[67]
- Patch-seq has been successfully applied to astrocytes in specific studies
- Whole-cell recordings measure electrophysiological heterogeneity (astrocytes don't fire action potentials but show electrical diversity)
- Examples: juxtavascular vs. non-juxtavascular astrocytes post-injury; morphologically distinct cortical plate vs. white matter astrocytes
- Limitation: requires prior labeling; useful for morphologically distinct subtypes

### Additional Regional and Specialized Datasets

**Darmanis et al. 2015 - Human Brain Cell Types**[68]
- **Species:** Human (*Homo sapiens*)
- **Regions:** Adult and fetal human brain
- **Method:** scRNA-seq
- **Cell numbers:** 466 cells
- **Multimodal:** No (transcriptomics only)
- **Download:** Check PNAS 2015 publication
- **Notes:** Early comprehensive survey identifying astrocytes, oligodendrocytes, neurons, microglia, endothelial cells

**Zeisel et al. 2015 - Mouse Brain Cell Types**[69][70][71]
- **Species:** Mouse (*Mus musculus*)
- **Regions:** Cortex and hippocampus
- **Method:** STRT-Seq with UMIs
- **Cell numbers:** ~3,000 cells
- **GEO Accession:** GSE60361
- **Download:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60361
- **Access via Bioconductor:** ZeiselBrainData() in scRNAseq package
- **Multimodal:** No (transcriptomics only)
- **Notes:** Foundational study; identifies astrocyte subpopulations; publicly available through multiple platforms

**Diverse Regional Studies - Additional GEO Accessions:**
- **GSE149598:** Human iPSC-derived astrocytes (maturation-enhancing protocols)[72]
- **GSE84826:** Human adult astrocytes (small molecule neuronal reprogramming)[73]
- **GSE207929:** Mouse astrocytic dysfunction in optic neuropathy[74]
- **GSE253640:** Mouse astrocytes - primary cilia signaling (cortex and cerebellum)[75]
- **GSE185472:** Human glia-enriched cortical organoids (xenotransplanted)[76]

### Data Integration and Analysis Resources

**Online Searchable Databases:**
- **GliaSeq (Liddelow Lab):** https://www.liddelowlab.com/gliaseq - Reactive astrocytes, rodent/human CNS glia, aging astrocytes, human iPSC-derived astrocytes[77]
- **BrainPalmSeq:** https://brainpalmseq.med.ubc.ca/ - Includes Batiuk astrocyte dataset with heatmap visualization[78]
- **Astrocyte RNA-Seq Browser (Denk Lab):** Mouse spinal cord injury astrocyte data - https://astrocyte.rnaseq (note: FPKM levels provided without cutoffs)[79]

**Multi-Study Integration Resources:**
- **STAB2:** Spatio-temporal cell atlas of human and mouse brain (19 human publications, 9 mouse publications; 1.5M human cells, 2.3M mouse cells)[80]
- **scRNA-Seq Datasets (Hemberg Lab):** https://hemberg-lab.github.io/scRNA.seq.datasets/ - Curated collection including mouse brain astrocyte studies[71]

### Key Notes on Data Access

1. **Species Coverage:** Extensive mouse datasets; growing human data, particularly from postmortem tissue and iPSC-derived cultures

2. **Multimodal Integration:** 
   - Transcriptomics + spatial: Bayraktar 2020, Yao 2023 (Allen), Scott 2024, Zhang 2024
   - Transcriptomics + chromatin: Frazel 2023, Yao 2024 (retina)
   - Transcriptomics + morphology: Endo 2022, Patch-seq approaches
   - Transcriptomics + electrophysiology + morphology: Patch-seq datasets

3. **File Formats:** Most datasets available as:
   - Raw: FASTQ files via SRA
   - Processed: Count matrices (TSV, CSV, MTX)
   - Analysis-ready: AnnData (.h5ad), Seurat objects (.rds, .h5seurat)
   - Metadata: Excel, CSV, or JSON

4. **Download Methods:**
   - Direct FTP links from GEO supplementary files
   - SRA Toolkit for raw sequencing data
   - Python packages: AbcProjectCache (Allen data), scanpy
   - R packages: GEOquery, scRNAseq (Bioconductor)
   - Interactive portals: CELLxGENE, Allen Brain Cell Atlas

5. **Data Preprocessing:** Most datasets provide:
   - Quality-filtered cells
   - Cell type annotations
   - Normalized expression matrices
   - UMAP/tSNE coordinates
   - Marker genes for each cluster

This comprehensive resource covers the major publicly available single-cell transcriptomics datasets for astrocytes, spanning multiple species, brain regions, developmental stages, and disease states, with specific emphasis on multimodal approaches that link transcriptomics to spatial location, morphology, electrophysiology, or chromatin state.

[1](https://www.nature.com/articles/s41467-019-14198-8)
[2](https://escholarship.org/content/qt6x31m2h7/qt6x31m2h7.pdf)
[3](https://pubmed.ncbi.nlm.nih.gov/32203496/)
[4](https://pubmed.ncbi.nlm.nih.gov/36378959/)
[5](https://authors.library.caltech.edu/records/1w82f-14a30/latest)
[6](https://www.nature.com/articles/s41586-023-06812-z)
[7](https://pmc.ncbi.nlm.nih.gov/articles/PMC10081189/)
[8](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246717)
[9](https://data.humancellatlas.org/hca-bio-networks/nervous-system/atlases/brain-v1-0)
[10](https://pmc.ncbi.nlm.nih.gov/articles/PMC10135484/)
[11](https://pubmed.ncbi.nlm.nih.gov/37189441/)
[12](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE73721)
[13](http://www2.neuroscience.umn.edu/eanwebsite/PDF%20GJClub/Neuron%2089%201%202016.pdf)
[14](https://www.nature.com/articles/s41593-024-01791-4)
[15](https://www.biorxiv.org/content/10.1101/2021.12.07.471509v2)
[16](https://pubmed.ncbi.nlm.nih.gov/37697111/)
[17](https://www.nature.com/articles/s41593-023-01424-2)
[18](https://pmc.ncbi.nlm.nih.gov/articles/PMC10763608/)
[19](https://pure.johnshopkins.edu/en/publications/longitudinal-scrna-seq-analysis-in-mouse-and-human-informs-optimi)
[20](https://www.nature.com/articles/s41597-024-03823-x)
[21](https://pmc.ncbi.nlm.nih.gov/articles/PMC11387634/)
[22](https://www.biorxiv.org/content/10.1101/2025.07.17.665323v1)
[23](https://www.biorxiv.org/content/10.1101/2025.07.17.665323v1.full-text)
[24](https://pmc.ncbi.nlm.nih.gov/articles/PMC12141159/)
[25](https://pmc.ncbi.nlm.nih.gov/articles/PMC10816327/)
[26](https://singlecell.broadinstitute.org/single_cell/study/SCP795/a-transcriptomic-atlas-of-the-mouse-cerebellum)
[27](https://elifesciences.org/articles/92046)
[28](https://rupress.org/jem/article/218/8/e20210040/212391/Single-cell-analysis-of-the-cellular-heterogeneity)
[29](https://pmc.ncbi.nlm.nih.gov/articles/PMC10511029/)
[30](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202627)
[31](https://pmc.ncbi.nlm.nih.gov/articles/PMC11787598/)
[32](https://pmc.ncbi.nlm.nih.gov/articles/PMC5782816/)
[33](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87544)
[34](https://pubmed.ncbi.nlm.nih.gov/28355573/)
[35](https://portals.broadinstitute.org/single_cell/study/a-molecular-census-of-arcuate-hypothalamus-and-median-eminence-cell-types)
[36](https://pmc.ncbi.nlm.nih.gov/articles/PMC10889077/)
[37](https://www.nature.com/articles/s41598-024-66044-7)
[38](https://pmc.ncbi.nlm.nih.gov/articles/PMC7813554/)
[39](https://www.pnas.org/doi/10.1073/pnas.2107339119)
[40](https://www.nature.com/articles/s41467-019-12780-8)
[41](https://pmc.ncbi.nlm.nih.gov/articles/PMC9817153/)
[42](https://academic.oup.com/proteincell/article/14/8/603/7049315)
[43](https://pmc.ncbi.nlm.nih.gov/articles/PMC11547256/)
[44](https://www.nature.com/articles/s41467-024-49133-z)
[45](https://www.biorxiv.org/content/10.1101/2023.09.08.556944v1.full-text)
[46](https://www.biorxiv.org/content/10.1101/2023.09.08.556944v2.full.pdf)
[47](https://bmblx.bmi.osumc.edu/ssread/help/faq)
[48](https://pmc.ncbi.nlm.nih.gov/articles/PMC12220722/)
[49](https://ngdc.cncb.ac.cn/databasecommons/database/id/9191)
[50](https://bmblx.bmi.osumc.edu/ssread/)
[51](https://www.nature.com/articles/s41467-024-45821-y)
[52](https://pmc.ncbi.nlm.nih.gov/articles/PMC10882052/)
[53](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182307)
[54](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494225/)
[55](https://www.semanticscholar.org/paper/Neuroinflammatory-astrocyte-subtypes-in-the-mouse-Hasel-Rose/595bddcb00e78ecce3dbcc61147d6bea5e9d33b5)
[56](https://pmc.ncbi.nlm.nih.gov/articles/PMC7880286/)
[57](https://elifesciences.org/articles/65482)
[58](https://pmc.ncbi.nlm.nih.gov/articles/PMC11397821/)
[59](https://www.biorxiv.org/content/10.1101/2020.11.04.369082v1.full-text)
[60](https://pmc.ncbi.nlm.nih.gov/articles/PMC6187980/)
[61](https://pmc.ncbi.nlm.nih.gov/articles/PMC6096303/)
[62](https://pmc.ncbi.nlm.nih.gov/articles/PMC8428855/)
[63](https://pubmed.ncbi.nlm.nih.gov/34387544/)
[64](https://github.com/AllenInstitute/patchseqtools)
[65](https://portal.brain-map.org/cell-types/classes/multimodal-characterization)
[66](https://knowledge.brain-map.org/data/97XR43ZTYJ2CQED8YA6)
[67](https://pmc.ncbi.nlm.nih.gov/articles/PMC12420811/)
[68](https://www.pnas.org/doi/10.1073/pnas.1507125112)
[69](https://bioconductor.org/books/3.15/OSCA.workflows/zeisel-mouse-brain-strt-seq.html)
[70](https://figshare.com/s/2fec97de0665a4414b03)
[71](https://hemberg-lab.github.io/scRNA.seq.datasets/mouse/brain/)
[72](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149598)
[73](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84826)
[74](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/geo/query/acc.cgi?acc=GSE207929)
[75](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE253640)
[76](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185472)
[77](https://www.liddelowlab.com/gliaseq)
[78](https://brainpalmseq.med.ubc.ca/cell-types/astrocytes-batiuk-2016/)
[79](https://www.franziskadenk.com/resources)
[80](https://academic.oup.com/nar/article/52/D1/D1033/7334093)
[81](https://pmc.ncbi.nlm.nih.gov/articles/PMC11409980/)
[82](https://pmc.ncbi.nlm.nih.gov/articles/PMC10157076/)
[83](https://nyuscholars.nyu.edu/en/publications/longitudinal-scrna-seq-analysis-in-mouse-and-human-informs-optimi)
[84](https://www.humancellatlas.org/publications/)
[85](https://www.science.org/doi/10.1126/sciadv.abe8978)
[86](https://www.science.org/doi/10.1126/science.adc9020)
[87](https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas)
[88](https://pmc.ncbi.nlm.nih.gov/articles/PMC11784854/)
[89](https://www.sciencedirect.com/science/article/pii/S2589004223022435)
[90](https://www.nature.com/articles/s41467-025-63429-8)
[91](https://www.biostars.org/p/9597785/)
[92](https://community.brain-map.org/t/how-do-i-download-specific-cell-type-gene-expression-data-from-whb/3648)
[93](https://alleninstitute.github.io/abc_atlas_access/intro.html)
[94](https://www.10xgenomics.com/spatial-transcriptomics)
[95](https://github.com/AllenInstitute/abc_atlas_access/blob/main/intro.md)
[96](https://satijalab.org/seurat/articles/spatial_vignette.html)
[97](https://alleninstitute.github.io/abc_atlas_access/descriptions/WMB-taxonomy.html)
[98](https://www.10xgenomics.com/platforms/visium)
[99](https://www.embopress.org/doi/10.1038/s44319-025-00529-y)
[100](https://www.biorxiv.org/content/10.1101/2023.11.12.566710v2.full-text)
[101](https://github.com/AllenInstitute/abc_atlas_access)
[102](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00363/full)
[103](https://www.10xgenomics.com/datasets)
[104](https://pmc.ncbi.nlm.nih.gov/articles/PMC7985878/)
[105](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114000)
[106](https://pmc.ncbi.nlm.nih.gov/articles/PMC9265979/)
[107](https://pmc.ncbi.nlm.nih.gov/articles/PMC5748686/)
[108](https://www.biorxiv.org/content/10.1101/839811v4.full-text)
[109](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8200306)
[110](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1146147/full)
[111](https://www.ncbi.xyz/geo/query/acc.cgi?acc=GPL21626)
[112](https://www.nature.com/articles/s41582-023-00809-y)
[113](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/geo/query/acc.cgi?acc=GSM8567272)
[114](https://www.nature.com/articles/s41598-024-74732-7)
[115](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873482/)
[116](https://pmc.ncbi.nlm.nih.gov/articles/PMC8842985/)
[117](https://www.nature.com/articles/sdata2018160)
[118](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1211079/full)
[119](https://pubmed.ncbi.nlm.nih.gov/37996532/)
[120](https://www.sciencedirect.com/science/article/pii/S2211124722000444)
[121](https://alleninstitute.github.io/abc_atlas_access/descriptions/MERFISH-C57BL6J-638850.html)
[122](https://www.nature.com/articles/s41593-025-01878-6)
[123](https://www.pnas.org/doi/10.1073/pnas.1912459116)
[124](https://zenodo.org/records/15127709)
[125](https://www.nature.com/articles/s41467-023-39447-9)
[126](https://www.nature.com/articles/s41586-023-07011-6)
[127](https://www.omicsdi.org/dataset/geo/GSE9566)
[128](https://www.biorxiv.org/content/10.1101/2023.11.30.569500v1.full-text)
[129](https://pmc.ncbi.nlm.nih.gov/articles/PMC5504258/)
[130](https://www.biorxiv.org/content/10.1101/2023.11.30.569500v1.full.pdf)
[131](https://pmc.ncbi.nlm.nih.gov/articles/PMC4840019/)
[132](https://www.youtube.com/watch?v=BQTHgwsrv2w)
[133](https://www.sciencedirect.com/science/article/pii/S0896627317305536)
[134](https://www.nature.com/articles/s41467-023-43568-6)
[135](https://www.pnas.org/doi/10.1073/pnas.2413140122)
[136](https://www.semanticscholar.org/paper/Molecular-diversity-of-astrocytes-Baldwin/e74d92a9c8099e7397b0bda507bb95e90b2549c0)
[137](https://onlinelibrary.wiley.com/doi/full/10.1002/glia.24434)
[138](https://pmc.ncbi.nlm.nih.gov/articles/PMC12419112/)
[139](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140822)
[140](https://www.embopress.org/doi/10.15252/embj.2018100811)
[141](https://www.biorxiv.org/content/10.1101/2021.12.07.471509v2.full-text)
[142](https://github.com/vitkl/cortical_astrocyte_mapping)
[143](https://www.nature.com/articles/s41598-023-32058-w)
[144](https://www.sciencedirect.com/science/article/pii/S2211124721009384)
[145](https://db.cngb.org/data_resources/project/PRJNA548917)
[146](https://www.nature.com/articles/s43587-022-00246-4)
[147](https://www.science.org/doi/10.1126/sciadv.adf6251)
[148](https://db.cngb.org/data_resources/project/PRJNA459483)
[149](https://elifesciences.org/articles/70514)
[150](https://rupress.org/jcb/article/222/11/e202303138/276267/Catenin-controls-astrocyte-morphogenesis-via-layer)
[151](https://github.com/FrancisCrickInstitute/Lattke_et_al_Astrocyte_Maturation)
[152](https://www.biorxiv.org/content/10.1101/2024.11.11.622998v2.full.pdf)
[153](https://onlinelibrary.wiley.com/doi/10.1002/glia.24479)
[154](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1211079/pdf)
[155](https://onlinelibrary.wiley.com/doi/10.1002/glia.24494)
[156](https://www.biccn.org/science/whole-mouse-brain)
[157](https://www.nature.com/articles/s41586-021-03950-0)
[158](https://www.refine.bio/experiments/SRP090730/single-cell-rna-seq-reveals-hypothalamic-cell-diversity)
[159](https://alleninstitute.github.io/abc_atlas_access/descriptions/WMB-10Xv3.html)
[160](https://d-nb.info/1279576073/34)
[161](https://community.brain-map.org/t/selecting-more-than-100-cells/4503)