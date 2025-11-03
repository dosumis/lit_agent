# Mapping Astrocyte Transcriptomic Types to Classical Identities

## Cerebellar Astrocytes -- Bergmann Glia

One clear mapping is the **cerebellar astrocyte cluster** (Astro-CB) to
**Bergmann glial cells**, the specialized astrocytes of the cerebellum.
The extended annotation file shows a single astrocyte cluster in the
cerebellum (Cluster 5207, "Astro-CB NN_1") enriched in the cerebellar
cortex (annotated "CB") with marker genes *Dao* (D-amino acid oxidase)
and *Efemp1*. These features strongly suggest Bergmann glia identity. In
the literature, Bergmann glia are known radial astrocytes of the
cerebellar molecular layer that highly express
DAO[\[1\]](https://pubmed.ncbi.nlm.nih.gov/2891417/#:~:text=The%20localization%20of%20D,containing%20processes%20of).
The Allen atlas data likewise indicate that cerebellar astrocytes have
unique molecular signatures -- for example, Pax3 is expressed in
Astro-CB cells (cerebellar astrocytes), distinct from telencephalic
astrocytes, and the transcription factor Nkx2-2 is specifically enriched
in Bergmann
glia[\[2\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=class%2C%20additional%20transcription%20factors%20mark,is%20specific%20to%20CHOR%20cells).
This aligns with the cluster's cerebellum-restricted location and DAO
marker: DAO activity localizes to Bergmann glial processes surrounding
Purkinje
cells[\[1\]](https://pubmed.ncbi.nlm.nih.gov/2891417/#:~:text=The%20localization%20of%20D,containing%20processes%20of).
Together, the spatial annotation ("CB") and marker profile (DAO\^high\^)
of cluster 5207 coincide with known properties of Bergmann glia in the
literature.

**Further validation:** To solidify this mapping, one could verify that
the cluster's markers are co-expressed in cerebellar Bergmann glia *in
situ*. For instance, immunostaining or MERFISH spatial transcriptomics
could test co-localization of **DAO** or **Pax3** with classic Bergmann
glia morphology (radial processes in the Purkinje layer). Additionally,
comparing this cluster's transcriptome with independent single-cell
datasets (e.g. the whole-cerebellum astrocyte profiles in Endo *et al.*
2022) would confirm if genes like **Nkx2-2** or **Pax3** are uniquely
upregulated. If available, electrophysiological profiling of identified
Bergmann glia (through Patch-seq) could be used to see if their
transcriptomic signature matches cluster 5207, linking the taxonomy to
the well-known physiology of Bergmann glia (e.g. their role in glutamate
uptake and D-serine metabolism). Finally, leveraging the Allen Brain
Atlas spatial data, one might check that cells of this cluster localize
to the **Purkinje cell layer** and extend processes to the pia, as
expected for Bergmann glia, providing anatomical confirmation of the
identity.

## Non-telencephalic Astrocytes -- Regional and Surface-Associated Types

In the **diencephalon, midbrain, and hindbrain (non-telencephalon)**,
astrocytes also diversify into region-specific subtypes that map to
classical descriptions. The extended annotations highlight two broad
groups here: (1) **surface-associated, GFAP-rich astrocytes** at the
pial boundary, and (2) **parenchymal astrocytes** in deep regions (e.g.
thalamus, brainstem nuclei). Clusters 5208--5211 (Astro-NT NN_1) are all
annotated with "pia" locations (e.g. "HB/CB pia", "MB/HB pia") and
indeed show very high **Gfap** expression. Yao *et al.* note that these
non-telencephalic clusters at the brain surface likely correspond to
**interlaminar astrocyte (ILA)-like cells** outside the
cortex[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
In primates, ILAs are a distinct astrocyte subtype with cell bodies in
layer I and long processes, and while rodents have far fewer ILAs, the
presence of GFAP\^high\^ subpial astrocytes in midbrain/hindbrain
suggests an analogous population. The extended data support this:
cluster 5210 ("non-TE pia/ventricle") and others express
fibrous-astrocyte markers like *Gfap* and *Agt* (angiotensinogen),
consistent with classical **fibrous astrocytes** which reside in white
matter tracts and glia limitans. Thus, clusters 5208--5211 likely map to
**marginal astrocytes** at the brain surface (glia limitans externa),
fulfilling a similar role to ILAs (forming a GFAP-rich barrier at the
pia)[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).

The second group comprises **region-specific parenchymal astrocytes** in
non-telencephalic gray matter. For example, cluster 5215 is enriched in
the thalamus (annotated "TH") and cluster 5217 in cerebellar and
cochlear nuclei ("CBN VCO
DCO")[\[4\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=is%20specific%20to%20hippocampal%20region%C2%A0and%C2%A0CTXsp%2C,and%205230%20and%20clusters%20in).
These likely correspond to **protoplasmic astrocytes** of those regions,
but with unique regional gene expression. Notably, prior work by John
Lin *et al.* identified an astrocyte subset ("Population A") that was
**enriched specifically in thalamus and olfactory
bulb**[\[5\]](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full#:~:text=cultured%20with%20population%20C%20astrocytes,migratory%20potentials%20than%20population%20C)
-- a clear indication that thalamic astrocytes diverge molecularly from
cortical ones. In our data, the thalamus cluster 5215 expresses unique
genes (e.g. the developmental TF *Otx2* was detected in this cluster in
our analysis), supporting a distinct identity. Similarly, astrocytes in
hindbrain structures (e.g. cochlear nuclei, cluster 5217) show markers
like *Aqp4* and *Fbln5*, hinting at specialized interactions with the
auditory circuits or blood--brain barrier there. These observations echo
the literature that astrocytes **vary by brain region**, expressing
region-specific transcriptional regulators that mirror developmental
patterning. For instance, Yao *et al.* found that telencephalic
(Astro-TE) astrocytes express **Foxg1/Emx2** (forebrain developmental
factors), whereas cerebellar astrocytes express **Pax3**, reflecting
their rhombencephalic
origin[\[2\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=class%2C%20additional%20transcription%20factors%20mark,is%20specific%20to%20CHOR%20cells).
Likewise, astrocytes in midbrain/hindbrain likely maintain expression of
caudal homeodomain genes (our data suggest *Otx2*\^+\^ in cluster 5215),
consistent with their embryonic origin.

**Further validation:** To map these non-telencephalic astrocyte
clusters to classical types, one could perform **spatial co-expression
analyses** of key markers. For instance, the hypothesized ILAs of the
brainstem (clusters 5208--5211) can be tested by staining for **GFAP**
and a candidate marker like *Sfrp5* (secreted frizzled-related protein
5, found in these clusters) to see if a distinct subpial astrocyte layer
is labeled in hindbrain sections. High-resolution MERFISH data already
confirm that clusters 5208--5211 localize to the pial surface outside
the
telencephalon[\[6\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=stream70%20%2C%20159%2C72%20%20,to%20be%20ILAs%20outside%20telencephalon)
-- additional marker colocalization (e.g. GFAP with **Claudin-10**,
noted in cluster 5210, a junction protein) would show if these cells
form a continuous glial limitans. For the parenchymal astrocytes (e.g.
thalamus cluster 5215), one could compare their transcriptome to
astrocytes from other regions: **cross-dataset analysis** using the Endo
*et al.* (2022) CNS atlas or the John Lin (2017) FACS-defined
populations could identify overlaps (John Lin's Population A in
thalamus/OB might correspond to this cluster's gene
signature[\[5\]](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full#:~:text=cultured%20with%20population%20C%20astrocytes,migratory%20potentials%20than%20population%20C)).
Immunostaining for a unique thalamus astrocyte marker (such as **Otx2**
or *Unc13c*, which appears in cluster 5215) in combination with
pan-astrocyte markers (S100β or Aldh1L1) would confirm a specialized
astrocyte subset in the thalamus. Similarly, cluster 5217's identity
(astrocytes in cochlear nucleus and cerebellar nuclei) could be tested
by looking at those regions for co-expression of **Aqp4** and
**Fibulin-5** (Fbln5), which the cluster uniquely expresses.
Electrophysiological differences could also be probed: fibrous
astrocytes (like the pia/fiber tract cluster 5219 in telencephalon and
its brainstem analogs) might exhibit higher K\<sup\>+\</sup\> buffering
currents and coupling, so patch-clamp recordings from surface vs deep
astrocytes in midbrain could reveal functional correlates of these
transcriptomic types. Finally, integration of **single-nucleus RNA-seq
datasets** from specific regions (e.g. a dataset focusing on brainstem
astrocytes) with the Allen atlas clusters could help transfer
annotations -- if an external dataset labels an astro subcluster as
"medulla fibrous astrocyte" with similar markers, one can confidently
map that to our Astro-NT pia cluster.

## Telencephalic Astrocytes -- Protoplasmic, Fibrous, and Regional Subtypes

Historically, astrocytes in the forebrain (telencephalon) have been
classified into **protoplasmic astrocytes** (in gray matter) and
**fibrous astrocytes** (in white
matter)[\[7\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=our%20understanding%20of%20the%20molecular,brain%20regions%20has%20accumulated%2034%2C5).
The transcriptomic taxonomy now refines this picture, revealing multiple
telencephalic astrocyte subtypes corresponding to distinct regions and
niches. The extended annotations for Astro-TE clusters support this
refinement. For example, **cluster 5219 (Astro-TE NN_1)** is annotated
as "pia and fiber tract" and shows high **Gfap** expression. Yao *et
al.* report that this cluster localizes to the **telencephalic pia** and
indeed represents the rodent equivalent of **interlaminar astrocytes**
in
cortex[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
These cells likely also include fibrous astrocytes of subcortical white
matter (e.g. corpus callosum), as suggested by their presence in fiber
tracts. In other words, cluster 5219 corresponds to the classical
**GFAP-rich fibrous astrocyte** population of the forebrain, forming the
glial limiting membrane and populating white matter. On the other hand,
several Astro-TE clusters map to **protoplasmic astrocytes** in specific
gray-matter regions: Yao *et al.* highlight that cluster 5225 is
specific to the **isocortex (neocortex) and olfactory areas**, cluster
5227 to the **dorsal striatum**, cluster 5226 to **septal and midline
regions**, and cluster 5228 to **hippocampal cortex (especially
subplate)**[\[8\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,path%20of%20the%20rostral%20migratory).
This means that the transcriptomic atlas has partitioned what we'd
broadly call "protoplasmic astrocytes" into region-defined types. Such a
finding is in line with emerging literature -- for instance, Batiuk *et
al.* (2020) identified **five transcriptomically distinct astrocyte
subtypes** in the adult mouse forebrain (cortex and
hippocampus)[\[9\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=five%20distinct%20Astrocyte%20SubTypes%20,In).
Those subtypes (AST1--AST5) showed clear regional biases, with some
subtypes predominantly in cortex and others in hippocampus, and each
subtype occupying distinct spatial domains in
situ[\[10\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=AST1%20and%20AST4%20being%20predominantly,Supplementary%20Data%201%20and%20https%3A%2F%2Fholt)[\[11\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=reveals%20distinct%20spatial%20positioning%20of,are%20available%20through%20an%20online).
This provides independent evidence that cortical astrocytes are
molecularly distinct from, say, striatal or hippocampal astrocytes,
rather than all being one homogeneous "protoplasmic" group. In fact, the
Batiuk study demonstrated **unique marker genes** for each subtype --
e.g. one subtype enriched for *Slc10a6* and other cortex-specific genes,
another enriched for cell-cycle genes in the hippocampus -- and
confirmed via RNAscope that these astrocyte subpopulations reside in
different brain
regions[\[11\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=reveals%20distinct%20spatial%20positioning%20of,are%20available%20through%20an%20online).
The Allen atlas data mirror this: each Astro-TE cluster has a unique
gene fingerprint (*Crym* and NMDA receptor subunit Grin2c in striatal
astrocytes, vs. *Zic4* and *Ranbp3l* in septal astrocytes, etc., from
the cluster markers) and a distinct anatomical
distribution[\[12\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,and%205230%20and%20clusters%20in).
For example, cluster 5227 (STRd astrocytes) expresses *Crym* (crystallin
μ) which is known to be high in striatal astrocytes relative to cortical
ones, whereas cluster 5225 (cortical astrocytes) expresses different
channels like *Kcnq3* and receptors like *S1pr1* relevant to cortex
function. This correspondence between location and gene profile confirms
that we are observing classical **protoplasmic astrocytes subdivided by
region**.

It's also worth noting the special case of **cortical layer I
astrocytes**. The dataset's "CTX pia sparse" clusters (e.g. 5218, 5220,
5221 in Astro-TE NN_1) likely represent the **sparse interlaminar
astrocytes in the rodent cortex**. In primates, interlaminar astrocytes
(ILAs) are abundant in layer I, but rodents have only a few such cells.
The annotation "pia sparse" and the high GFAP levels of cluster 5219
(mentioned above) suggest that rodent layer I astrocytes were detected
as a distinct transcriptomic
group[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
These cells also express markers like *Myoc* (myocilin) and *Lhx2* (a
developmental transcription factor) per the cluster data, which might
indicate a less mature or specialized state. Although ILAs are not
well-characterized in mouse literature due to their rarity, the **Allen
MERFISH data** did confirm a cluster of telencephalic astrocytes at the
pia with high
Gfap[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
Thus, this cluster mapping revives the notion of ILAs in rodents,
aligning a transcriptomic type with a classical morphological category
(astrocytes with vertical processes in layer
I)[\[13\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=interlaminar%20astrocytes%C2%A0%28ILAs%2973,to%20be%20ILAs%20outside%20telencephalon).

**Further validation:** To explore these telencephalic mappings, one can
use both **spatial transcriptomics and targeted experiments**. For the
fibrous astrocyte cluster (5219), **co-labeling for GFAP and an
identified marker like Ddn** (Dendrin, present in 5219) in corpus
callosum or subpial cortex would test if those cells correspond to the
transcriptomic cluster. We expect these fibrous astrocytes to line the
pia and populate white matter; MERFISH images (Fig. 4b in Yao *et al.*)
already show cluster 5219 at the telencephalic
surface[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
Similarly, to distinguish the regional protoplasmic astro types, one
could pick marker genes unique to each cluster and perform **multiplexed
RNA in situ hybridization**. For instance: **Crym** for striatal
astrocytes vs. **Fam163a** for cortical astrocytes (cluster 5225) vs.
**Cxcl5** for the septal/hippocampal-enriched cluster 5224 -- applying
these probes to forebrain sections would reveal non-overlapping
patterns, reflecting each subtype's territory (striatal, cortical,
septal, etc.). The Allen Brain Atlas's own platform might allow one to
visualize these gene expression distributions to double-check the
co-location with known regions. Another approach is **single-cell
integration analysis**: for example, taking the scRNA-seq data from
Batiuk *et al.* (available online) and seeing if their AST2
(cortex-preferring) cluster's top genes overlap with our cluster 5225's
markers (which they likely do, as both represent cortical astrocytes).
If there's strong gene set enrichment overlap, it reinforces the mapping
of cluster 5225 to "cortical protoplasmic astrocyte subtype".
Conversely, Batiuk's AST1 (hippocampal) should align with clusters
5222/5223 (DG astro) or 5228 (HIP/CTXsp) -- checking markers like
**Sparc** or **Gpc5** that were noted for hippocampal astrocytes in that
study against our data would be informative. In addition,
**electrophysiological or morphological assays** could test if these
subtypes have different functional properties: e.g. do cortical
astrocytes (cluster 5225) show different calcium signaling or synaptic
ensheathment properties compared to striatal astrocytes (cluster 5227)?
Patch-clamp recordings combined with RNA-seq (Patch-seq) in acute slices
could correlate functional differences with transcriptomic cluster
identity -- a forward-looking experiment that has been suggested as a
way to align transcriptomic subtypes with
physiology[\[14\]](https://www.embopress.org/doi/10.1038/s44319-025-00529-y#:~:text=Astrocyte%20diversity%20and%20subtypes%3A%20aligning,cell).
Lastly, **developmental or lineage tracing studies** could provide
evidence: since telencephalic astrocytes (Astro-TE) express Emx2/Foxg1
and subpallial ones might express Nkx2-1 or other markers, fate-mapping
those lineages might show that, for example, Emx2-lineage astrocytes
correspond to the cortical clusters while Nkx2-1-lineage (basal
forebrain-derived) correspond to striatal or septal astro clusters. This
would biologically validate that the transcriptomic segregation indeed
reflects developmental origin, as the literature
suggests[\[15\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=regulators%20of%20neurogenesis%20in%20the,is%20specific%20to%20CHOR%20cells).

## Neurogenic Niche Astrocytes -- Dentate Gyrus Radial Glia and SVZ Astrocytes

A particularly interesting mapping emerges for astrocytes in the adult
**neurogenic niches**: the subgranular zone of the dentate gyrus (DG) in
the hippocampus, and the subventricular zone (SVZ) of the lateral
ventricles. In the atlas, **two clusters (5222 and 5223, Astro-TE
NN_2)** are specific to the dentate
gyrus[\[16\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=astrocyte%20clusters%20exhibit%20further%20subregion,DCO%29%20and).
These likely correspond to the **radial glia-like neural stem
astrocytes** in the DG, often called type 1 or SGZ astrocytes. The
annotation "DG" and the marker profile support this: for instance,
cluster 5223 highly expresses *Mcm6* and *Egfr*, which are associated
with proliferating progenitor cells (Mcm6 is a DNA replication factor,
EGFR is known to mark activated neural stem cells in both SVZ and SGZ).
In contrast, cluster 5222 (also DG) expresses genes like *Slc39a12* and
a novel transcript **Gm6145**, potentially representing a more quiescent
astrocyte state in the SGZ. Literature provides strong concordance:
Batiuk *et al.* identified an astrocyte subtype "AST4" characterized by
a high fraction of cell-cycle and proliferation genes, which they
**hypothesized to be neural stem astrocytes**. They confirmed that AST4
astrocytes reside in the DG's subgranular zone, comprising the majority
of Slc1a3\^+\^ (GLAST-positive) stem-like astrocytes
there[\[17\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=Atlas%20%28Supplementary%20Fig,general%20marker%20of%20stem%20cells)[\[18\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=match%20at%20L424%20AST4%20localizes,based%20mapping).
Notably, AST4 cells expressed Ascl1 (a progenitor marker) and other
proliferation genes, very much like our cluster 5223 does. This is a
direct literature parallel: the DG clusters in the Allen atlas coincide
with the classical **SGZ radial astrocyte** phenotype -- GFAP\^+\^,
Sox2\^+\^, stem-cell like astrocytes that generate new granule
neurons[\[19\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Cell%20proliferation%20and%20neuronal%20differentiation,neuron%20subclasses%20in%20OB28%20to).

Similarly, the atlas delineates astrocyte clusters along the
**SVZ--Rostral Migratory Stream (RMS)--Olfactory Bulb (OB)** axis.
**Clusters 5229 and 5230 (Astro-TE NN_5)** are annotated in SVZ regions
(e.g. "SVZ STRd AON" meaning SVZ near dorsal striatum and anterior
olfactory nucleus). These are clearly the **SVZ astrocytes (type B
cells)** that serve as ventricular-zone neural stem cells. They express
stemness and patterning genes (*Thbs4*, *Sfrp1*, etc.) and are spatially
located along the lateral
ventricles[\[20\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=specific%20to%20LSX%20and%20midline,5208%2C%205209%2C%205210%20and).
Yao *et al.* observed that these clusters, together with the Astro-OLF
clusters in the olfactory bulb, form a trajectory in UMAP space
corresponding to the **migration from SVZ to
OB**[\[21\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match)[\[20\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=specific%20to%20LSX%20and%20midline,5208%2C%205209%2C%205210%20and).
Indeed, clusters 5231--5236 (Astro-OLF NN_1-3) are found in the main
olfactory bulb (MOB), with some closer to the RMS entry ("MOB core") and
others in outer layers. This mirrors the known biology: SVZ astrocytes
(type B) give rise to transient amplifying cells (type C) and
neuroblasts (type A) that migrate through the RMS to the OB. During this
migration, specialized astrocytes line the path and form "glial tubes"
guiding the
neuroblasts[\[22\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match).
The presence of a continuum of astrocyte transcriptomic changes from SVZ
(clusters 5229--5230) through to OB (clusters 5231--5236) exactly
reflects this phenomenon. In fact, Yao *et al.* report that along the
RMS path, astrocytes in their data show gradations in gene expression
similar to the gradient in immature neurons, with dozens of genes
changing along the
trajectory[\[23\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=OB%C2%A0neurons%20are%20marked%20by%20the,genes%20that%20are%20differentially%20expressed).
This strongly suggests that cluster 5229/5230 map to **SVZ B1
astrocytes**, and clusters 5231--5236 map to **RMS/OB astrocytes** that
interact with migrating neurons. Classical markers also coincide: SVZ B1
astrocytes are known to express **GFAP, Prom1 (CD133), GLAST, FGFR3**
and other radial glia genes, many of which (e.g. *Gfap*, *Sox2*) are
also highlighted as being expressed in these astro
subclasses[\[24\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=clusters%20express%20radial%20glia%20marker,AP78%20%2C%20167%2C80%20%2C%20169).
Our cluster data show *Sox2* in the Astro-Epen class generally and
*Thbs4* upregulated in SVZ astro, consistent with a quiescent neural
stem cell astrocyte that secretes factors like thrombospondin-4.
Additionally, Rax, a transcription factor, is noted by Yao *et al.* as
specific to tanycytes (hypothalamic radial
glia)[\[25\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=and%20neurons%20are%20derived%20from,is%20specific%20to%20CHOR%20cells),
whereas **Lef1** is specific to CHOR cells -- these are
ependymal-related, but interestingly, the SVZ astro niches (particularly
in the OB core) might show Wnt-signaling differences (Lef1 is a Wnt
pathway TF often active in OB neurogenic niche). While those details are
beyond our scope, the key point is that *multiple lines of evidence
converge on identifying these clusters as the known neural stem cell
astrocytes*. The DG clusters match the SGZ radial glial astrocyte
described in many studies, and the SVZ/OLF clusters map onto the known
B1 astrocytes and their downstream astroglial network in the
RMS[\[19\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Cell%20proliferation%20and%20neuronal%20differentiation,neuron%20subclasses%20in%20OB28%20to).

**Further validation:** To test these mappings, researchers could pursue
both **molecular and functional analyses**. On the molecular side,
checking for co-expression of **neural stem cell markers** in these
clusters' spatial locations would be compelling. For example, in the
dentate gyrus, one could perform triple-label in situ for **GFAP**,
**SOX2**, and a cluster-specific marker like **Egfr** or **Mcm6** -- we
expect the SGZ cells (radial astrocytes) to be GFAP\^+/SOX2\^+ and
cycling (Mcm6\^+ in some). This would directly show that cluster 5223
corresponds to the dividing radial glia that have been
well-characterized (often called Type-1
progenitors)[\[17\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=Atlas%20%28Supplementary%20Fig,general%20marker%20of%20stem%20cells).
In the SVZ, one could label **GLAST (Slc1a3)** or GFAP along with
**Prominin-1 (Prom1)** to mark B1 cells, and see if those cells also
express a cluster marker like **Thbs4** or **Sfrp1** -- confirming that
the transcriptomic cluster captures the B1 cell population. The Allen
atlas MERFISH images (Extended Data Fig. 12 in Yao *et al.*) might
already show GFAP\^high\^ astrocytes lining the ventricles for these
clusters[\[13\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=interlaminar%20astrocytes%C2%A0%28ILAs%2973,to%20be%20ILAs%20outside%20telencephalon).
On a functional level, **lineage tracing** or birth-dating experiments
could be done: if cluster 5223 truly are neural stem astrocytes, they
should incorporate labels like BrdU and give rise to new neurons. One
could inject BrdU and see if BrdU-positive astrocytes in SGZ express the
cluster's signature genes (maybe via single-cell qPCR or RNAscope).
Similarly, in SVZ, tracing B1 cells (for example using a GFAP-CreER
driver to mark quiescent NSCs) and then performing single-cell RNA-seq
on those marked cells could validate that their transcriptomes align
with clusters 5229/5230. **External datasets** can also aid annotation:
for instance, the single-cell study by Basak *et al.* or others on adult
SVZ stem cells could be cross-referenced -- do their "quiescent B1" and
"active B1" clusters express the same top genes as our clusters 5229 vs
5230? If yes, that's a strong transfer of annotation (e.g., if one
cluster has more *Aspm/Mki67* and corresponds to active dividing B1,
whereas the other is quiescent). Patch-seq could even be applied here in
an unconventional way: although these astroglial cells are not typically
characterized electrophysiologically in detail, one might assess their
membrane properties (which tend to be different for stem astrocytes --
they often have relatively depolarized resting potentials and low
K\<sup\>+\</sup\> conductance compared to mature astrocytes). By
patching an SVZ astro vs a cortical astro and then sequencing it, one
could see if the SVZ astro's RNA profile matches cluster 5229/5230.
Lastly, **spatial lineage mapping** via techniques like BARseq or serial
two-photon imaging could track cells from the SVZ clusters migrating to
OB -- if the astrocytes along the RMS indeed correspond to cluster
5231--5236, they might upregulate certain genes (our data show *Il33*
and *Chrdl1* in cluster 5231, for example) as they approach the OB.
Verifying such gene upregulation along the RMS in tissue (e.g.
increasing IL-33 immunoreactivity in astrocytes nearer the OB) would
further support the idea that the transcriptomic trajectory captures a
maturation or positional gradient, cementing the identity of these cells
as the supportive astrocytes of the RMS. The rich resources of the Allen
Brain Cell Atlas (including MapMyCells and the Brain Knowledge Platform)
could also be leveraged to systematically compare these astrocyte
clusters with known cell types, potentially pulling in human data for
analogous cell types and thereby extending annotation transfer across
species.

## Olfactory Bulb Astrocytes and Rostral Migratory Stream Associations

The **olfactory bulb (OB) astrocytes** form the tail end of the SVZ--RMS
pathway and appear as the Astro-OLF subclass (clusters 5231--5236).
These clusters merit special mention, as they may map to astrocyte
subtypes in different layers of the OB. The extended annotations for
these clusters indicate localization in the main olfactory bulb (e.g.
"MOB mi" for mitral layer, "MOB out" for outer layers, "MOB core" for
core/inner OB). This suggests that the atlas distinguishes astrocytes in
the OB's distinct laminae -- possibly those associated with the
glomerular layer vs. the deeper granule cell layer. Classical anatomy
doesn't give separate names to astrocytes in different OB layers, but
functionally they might differ (astrocytes in the glomerular layer
interact with periglomerular neurons and olfactory nerve axons, whereas
deep OB astrocytes interact with migrating neuroblasts and granule
cells). The transcriptomic data provide clues: for instance, cluster
5231 (MOB "mi") expresses **Il33** and *Chrdl1*, whereas cluster 5234
(MOB inner) expresses *Sfrp1* and *Atp13a4*. IL-33 is a cytokine notably
produced by astrocytes that can regulate microglial activity during
synaptic pruning. Its high expression in an OB astrocyte cluster aligns
with reports that astrocyte-derived IL-33 is important for synapse
refinement in development (observed in other regions like thalamus, and
likely relevant in OB which undergoes adult neurointegration).
Meanwhile, *Sfrp1* (a Wnt signaling modulator) in inner OB astrocytes
might reflect their interaction with RMS neuroblasts, as Wnt signaling
is known to influence OB interneuron integration. These details
illustrate how the extended annotation markers coincide with
**literature assertions about astrocyte function**: OB astrocytes have
been implicated in neuroblast migration support and synaptogenesis, and
here we see migratory stream-associated genes and synapse-modulatory
genes in their profiles. Additionally, as noted earlier, John Lin *et
al.*'s study found a region-enriched astrocyte population in the
olfactory bulb (co-enriched with
thalamus)[\[5\]](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full#:~:text=cultured%20with%20population%20C%20astrocytes,migratory%20potentials%20than%20population%20C).
That corresponds well with the idea that OB astrocytes form a distinct
subtype, as captured by the Astro-OLF clusters. The fact that Population
A astrocytes (Lin 2017) were abundant in OB and TH suggests they had a
unique combination of surface markers or gene expression that set them
apart from cortical astrocytes -- our data now pin down what some of
those differences likely are (e.g., OLF astrocytes express genes like
*Ano1* and *Ecrg4* that we see in clusters 5231 and 5235, not typically
high in cortex).

From a spatial viewpoint, **astrocytes in the OB are positioned along
the RMS entry point** and throughout the bulb, and Yao *et al.*
explicitly mention that the trajectory of astrocyte clusters from SVZ
into OB aligns with spatial
gradients[\[26\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20trajectory%20of%20these%20astrocyte,Extended%20Data%20Fig)[\[20\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=specific%20to%20LSX%20and%20midline,5208%2C%205209%2C%205210%20and).
They also observed an "inside-out" gradient in the olfactory bulb for
certain non-neuronal cells
(OECs)[\[27\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20spatial%20distribution%20of%20all,148),
which hints that even within the OB, astrocyte subtypes might distribute
from core to periphery. In sum, the OB astrocyte clusters can be mapped
to **layer-specific astrocytes in the olfactory bulb** -- e.g., a
cluster for astrocytes near the mitral cell layer vs. one for astrocytes
in the granule cell layer. While classical literature doesn't name these
as separate types, it is known that the OB's unique structure and
continual neurogenesis endow its astrocytes with specialized roles
(supporting newborn neuron integration and possibly modulating odor
circuit plasticity). The transcriptome data now give us marker sets to
define those roles more precisely.

**Further validation:** Investigating the OB astrocyte subtypes could
leverage **layer-specific analyses in the bulb**. One experiment could
be a **layer-selective RNA profiling**: microdissect the glomerular
layer vs. granule cell layer of the OB and perform RNA-seq to see if the
signatures match clusters (e.g., does the glomerular layer sample show
higher *Il33* and *Ano1*, corresponding to cluster 5231?).
Alternatively, high-resolution in situ hybridization for markers like
**Il33 (cluster 5231)**, **Sfrp1 (cluster 5234/5236)**, and **Dipk1c
(cluster 5235)** on OB sections would allow us to map each marker to a
layer -- expecting, for example, Il33\^+\^ astrocytes in superficial OB
and Sfrp1\^+\^ astrocytes in the core. The Allen Atlas MERFISH data
likely already delineates these, but a focused validation can confirm
that these markers indeed delineate non-overlapping astrocyte
populations in the OB. Furthermore, since OB astrocytes are involved in
adult-born neuron integration, one could use **patch-seq on OB slices**:
identify an astrocyte in the OB (by morphology or location), patch-clamp
it to assess properties (like spontaneous Ca²⁺ activity or
K\<sup\>+\</sup\> buffering currents in that layer), then aspirate and
sequence it. Comparing the sequenced transcriptome to the cluster
centroids would tell us whether it was a "mitral layer astrocyte" vs
"granular layer astrocyte" by matching to clusters 5231/5232 vs
5233--5236, for instance. Additionally, given OB astrocytes may express
distinct neuropeptides or receptors (the file's `np.markers` could
contain candidates -- e.g. perhaps **Prodynorphin** or others if
present), one could look for those in known OB glia physiology. If, say,
one cluster expresses **Nts (neurotensin)** or a neuropeptide, that
could be tested by checking if OB astrocytes release or respond to that
neuropeptide in slice preparations. Lastly, integrating data from
**human or other species** could be illuminating: the Allen Human Brain
Atlas or recent single-nucleus RNA-seq from human olfactory bulb might
reveal analogous astrocyte subtypes. If those show a similar division
(e.g. one group IL33-high, another SFRP1-high), it strengthens the idea
that these are conserved cell types. New tools like MapMyCells or the
BICCN cell type comparison
platform[\[28\]](https://knowledge.brain-map.org/data/LVDBJAW8BI5YSS1QUBG#:~:text=ABC%20Atlas%20,brain)[\[29\]](https://www.science.org/doi/10.1126/science.add7046#:~:text=As%20a%20first%20step%20toward,throughout%20the%20entire%20human%20brain)
might allow a direct computational mapping of mouse OB astrocyte
clusters to any available human or non-human primate OB astrocyte data,
providing further evidence for their identity.

## Conclusion

In summary, by leveraging the extended annotations (markers,
neuropeptides, neurotransmitter predictions, and spatial distribution)
of the Allen Whole Brain atlas, we can map each astrocyte transcriptomic
type (t-type) to known astrocyte classes from the literature:

-   **Astro-CB (Cluster 5207)** maps to **Bergmann glia**, sharing
    location (cerebellar cortex) and markers like
    DAO[\[1\]](https://pubmed.ncbi.nlm.nih.gov/2891417/#:~:text=The%20localization%20of%20D,containing%20processes%20of)
    and
    Nkx2-2[\[25\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=and%20neurons%20are%20derived%20from,is%20specific%20to%20CHOR%20cells)
    unique to cerebellar astrocytes.
-   **Astro-NT (non-telencephalic) clusters** bifurcate into **fibrous,
    GFAP\<sup\>high\</sup\> subpial astrocytes** (ILA-like cells at
    brain
    surfaces)[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon)
    and **regional gray-matter astrocytes** (e.g. thalamus, brainstem)
    that align with known regional
    heterogeneity[\[5\]](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full#:~:text=cultured%20with%20population%20C%20astrocytes,migratory%20potentials%20than%20population%20C).
-   **Astro-TE (telencephalic) clusters** include the broad **fibrous
    astrocyte** population of cortex/white matter (GFAP-rich glial
    limitans, analogous to classical fibrous astrocytes) and multiple
    **protoplasmic astrocyte subtypes** segregated by region (cortical,
    striatal, septal, hippocampal), in agreement with recent single-cell
    studies showing spatially specialized astrocyte
    subtypes[\[11\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=reveals%20distinct%20spatial%20positioning%20of,are%20available%20through%20an%20online).
    Even sparse **interlaminar astrocytes** in the rodent cortex appear
    as a distinct cluster at the
    pia[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon).
-   **Neurogenic niche astrocytes** are captured as well: an **SGZ
    radial astrocyte** cluster in the dentate gyrus, matching the
    profile of stem-like astrocytes that express proliferation
    markers[\[17\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=Atlas%20%28Supplementary%20Fig,general%20marker%20of%20stem%20cells),
    and **SVZ astrocyte clusters** that form a continuum with **RMS and
    olfactory bulb astrocytes**, corresponding to the known migratory
    glial tubes and OB astrocyte network supporting adult
    neurogenesis[\[21\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match)[\[20\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=specific%20to%20LSX%20and%20midline,5208%2C%205209%2C%205210%20and).

Each of these mappings is supported by overlapping marker genes and
anatomical placement between the atlas data and prior literature. By
conducting targeted validation experiments (marker co-localization,
spatial transcriptomics, Patch-seq, cross-dataset comparisons, and
functional assays), these proposed identities can be tested. Moreover,
resources like patch-seq data (where available) and single-cell
transcriptomic datasets from specific brain regions or developmental
stages can be harnessed for **annotation transfer**, further
strengthening our confidence in the cell type mappings. For example,
integrating astrocyte profiles from a targeted SVZ single-cell study
could confirm which Allen cluster corresponds to quiescent vs active B1
astrocytes, or using the transcriptomes of Bergmann glia recorded via
patch-seq in cerebellar slices could directly link electrophysiological
phenotype to the Astro-CB cluster. As the atlas is already integrated
with the Common Coordinate Framework, one can also perform **in silico
colocalization** (as Yao *et al.* did for VLMC and ILA
interactions[\[30\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=VLMC%20types66%20%2C%20170%20also,cluster%205303%20does%20not%20express))
-- e.g. checking if pia-specific astrocyte clusters are spatially
adjacent to pia-specific VLMC (vascular leptomeningeal cells), which
they
are[\[31\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=patterns,cluster%205303%20does%20not%20express),
reinforcing the notion that those astrocytes are the glia limitans. All
these strategies will help convert the "potential mappings" we've
identified into firmly established relationships between new
transcriptomic cell types and the rich legacy of classical neuroglial
cell types.

By systematically combining transcriptomic evidence with classical
markers, location, and functional data, we can **confidently map the
astrocyte t-types to known identities**. This not only validates the
atlas annotations but also expands our understanding of astrocyte
diversity -- revealing, for instance, that even "canonical" protoplasmic
astrocytes come in multiple region-specific flavors, or that previously
nebulous categories like "astrocytes in the OB" actually consist of
multiple subtypes with distinct roles. The outcome of such mapping and
validation will be a more unified framework where classic glial biology
and modern single-cell genomics inform each other, ultimately clarifying
how each astrocyte subtype contributes to neural circuit function and
brain health.

**Sources:** The mappings and analyses above are supported by integrated
data from the Allen Brain Cell Atlas (whole mouse
brain)[\[32\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,TE%20cluster%205219%20is)[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon),
and are cross-referenced with key findings from recent literature on
astrocyte diversity, including region-specific astrocyte subtypes
identified by single-cell RNA
sequencing[\[9\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=five%20distinct%20Astrocyte%20SubTypes%20,In)[\[11\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=reveals%20distinct%20spatial%20positioning%20of,are%20available%20through%20an%20online),
classical studies of cerebellar Bergmann
glia[\[1\]](https://pubmed.ncbi.nlm.nih.gov/2891417/#:~:text=The%20localization%20of%20D,containing%20processes%20of),
and known properties of neurogenic niche astrocytes in the adult
brain[\[17\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=Atlas%20%28Supplementary%20Fig,general%20marker%20of%20stem%20cells)[\[22\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match).
These sources illustrate the convergence between transcriptomic clusters
and classical cell types, guiding the proposed mappings and suggested
validation experiments.

[\[1\]](https://pubmed.ncbi.nlm.nih.gov/2891417/#:~:text=The%20localization%20of%20D,containing%20processes%20of)
Localization of D-amino acid oxidase in Bergmann glial cells and
astrocytes of rat cerebellum - PubMed

<https://pubmed.ncbi.nlm.nih.gov/2891417/>

[\[2\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=class%2C%20additional%20transcription%20factors%20mark,is%20specific%20to%20CHOR%20cells)
[\[3\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20Astro,to%20be%20ILAs%20outside%20telencephalon)
[\[4\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=is%20specific%20to%20hippocampal%20region%C2%A0and%C2%A0CTXsp%2C,and%205230%20and%20clusters%20in)
[\[6\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=stream70%20%2C%20159%2C72%20%20,to%20be%20ILAs%20outside%20telencephalon)
[\[8\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,path%20of%20the%20rostral%20migratory)
[\[12\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,and%205230%20and%20clusters%20in)
[\[13\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=interlaminar%20astrocytes%C2%A0%28ILAs%2973,to%20be%20ILAs%20outside%20telencephalon)
[\[15\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=regulators%20of%20neurogenesis%20in%20the,is%20specific%20to%20CHOR%20cells)
[\[16\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=astrocyte%20clusters%20exhibit%20further%20subregion,DCO%29%20and)
[\[19\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Cell%20proliferation%20and%20neuronal%20differentiation,neuron%20subclasses%20in%20OB28%20to)
[\[20\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=specific%20to%20LSX%20and%20midline,5208%2C%205209%2C%205210%20and)
[\[21\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match)
[\[22\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20migrating%20neurons%20in%20the,OLF%20subclass%20%285231%E2%80%935236%29%20match)
[\[23\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=OB%C2%A0neurons%20are%20marked%20by%20the,genes%20that%20are%20differentially%20expressed)
[\[24\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=clusters%20express%20radial%20glia%20marker,AP78%20%2C%20167%2C80%20%2C%20169)
[\[25\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=and%20neurons%20are%20derived%20from,is%20specific%20to%20CHOR%20cells)
[\[26\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=the%20trajectory%20of%20these%20astrocyte,Extended%20Data%20Fig)
[\[27\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=The%20spatial%20distribution%20of%20all,148)
[\[30\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=VLMC%20types66%20%2C%20170%20also,cluster%205303%20does%20not%20express)
[\[31\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=patterns,cluster%205303%20does%20not%20express)
[\[32\]](https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50#:~:text=Astro,TE%20cluster%205219%20is)
A high-resolution transcriptomic and spatial atlas of cell types in the
whole mouse brain \| Nature

<https://www.nature.com/articles/s41586-023-06812-z?error=cookies_not_supported&code=5a7087c6-7cd3-41ee-939f-a0388a4d4f50>

[\[5\]](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full#:~:text=cultured%20with%20population%20C%20astrocytes,migratory%20potentials%20than%20population%20C)
Frontiers \| Commentary: Identification of diverse astrocyte populations
and their malignant analogs

<https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2017.00193/full>

[\[7\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=our%20understanding%20of%20the%20molecular,brain%20regions%20has%20accumulated%2034%2C5)
[\[9\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=five%20distinct%20Astrocyte%20SubTypes%20,In)
[\[10\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=AST1%20and%20AST4%20being%20predominantly,Supplementary%20Data%201%20and%20https%3A%2F%2Fholt)
[\[11\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=reveals%20distinct%20spatial%20positioning%20of,are%20available%20through%20an%20online)
[\[17\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=Atlas%20%28Supplementary%20Fig,general%20marker%20of%20stem%20cells)
[\[18\]](https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d#:~:text=match%20at%20L424%20AST4%20localizes,based%20mapping)
Identification of region-specific astrocyte subtypes at single cell
resolution \| Nature Communications

<https://www.nature.com/articles/s41467-019-14198-8?error=cookies_not_supported&code=b22dad85-b4a3-4f39-8179-1c32a398fc7d>

[\[14\]](https://www.embopress.org/doi/10.1038/s44319-025-00529-y#:~:text=Astrocyte%20diversity%20and%20subtypes%3A%20aligning,cell)
Astrocyte diversity and subtypes: aligning transcriptomics with \...

<https://www.embopress.org/doi/10.1038/s44319-025-00529-y>

[\[28\]](https://knowledge.brain-map.org/data/LVDBJAW8BI5YSS1QUBG#:~:text=ABC%20Atlas%20,brain)
ABC Atlas - Whole Mouse Brain - Brain Knowledge Platform

<https://knowledge.brain-map.org/data/LVDBJAW8BI5YSS1QUBG>

[\[29\]](https://www.science.org/doi/10.1126/science.add7046#:~:text=As%20a%20first%20step%20toward,throughout%20the%20entire%20human%20brain)
Transcriptomic diversity of cell types across the adult human brain

<https://www.science.org/doi/10.1126/science.add7046>
