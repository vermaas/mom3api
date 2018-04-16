# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dataproduct(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=20)
    released = models.IntegerField()
    exported = models.IntegerField(blank=True, null=True)
    fileformat = models.CharField(max_length=50, blank=True, null=True)
    archived = models.IntegerField(blank=True, null=True)
    pipelined = models.IntegerField(blank=True, null=True)
    topology = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    placeholder = models.IntegerField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataproduct'


class DataproductLocation(models.Model):
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    cluster_name = models.CharField(max_length=20, blank=True, null=True)
    cluster_partition = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataproduct_location'


class Dataproducttext(models.Model):
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    textid = models.ForeignKey('Text', models.DO_NOTHING, db_column='textid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataproducttext'


class Export(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    exportid = models.IntegerField(blank=True, null=True)
    nr_dataproducts = models.IntegerField(blank=True, null=True)
    nr_ingested = models.IntegerField(blank=True, null=True)
    nr_aborted = models.IntegerField(blank=True, null=True)
    percentage_ingested = models.IntegerField(blank=True, null=True)
    nr_source_location = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export'


class LofarAntennafield(models.Model):
    name = models.CharField(max_length=15)
    station_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_antennafield'


class LofarAveragingPipeline(models.Model):
    mom2objectid = models.IntegerField(blank=True, null=True)
    flagging_strategy = models.CharField(max_length=50, blank=True, null=True)
    frequency_integration_step = models.IntegerField(blank=True, null=True)
    time_integration_step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_averaging_pipeline'


class LofarBbsParameters(models.Model):
    baselines = models.CharField(max_length=100, blank=True, null=True)
    correlations = models.CharField(max_length=100, blank=True, null=True)
    beam_model_enable = models.IntegerField(blank=True, null=True)
    solve_parms = models.CharField(max_length=100, blank=True, null=True)
    solve_uvrange = models.CharField(max_length=100, blank=True, null=True)
    strategy_baselines = models.CharField(max_length=40, blank=True, null=True)
    strategy_timerange = models.CharField(max_length=100, blank=True, null=True)
    lofar_pipeline_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_bbs_parameters'


class LofarBeamMeasurement(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    spec_targetname = models.CharField(max_length=100)
    spec_ra = models.FloatField(blank=True, null=True)
    spec_decl = models.FloatField(blank=True, null=True)
    spec_equinox = models.CharField(max_length=10, blank=True, null=True)
    spec_duration = models.FloatField(blank=True, null=True)
    spec_sub_central_frequency = models.FloatField(blank=True, null=True)
    spec_sub_bandwidth = models.FloatField(blank=True, null=True)
    spec_sub_contiguous = models.IntegerField(blank=True, null=True)
    spec_sub_custom_subbands = models.IntegerField(blank=True, null=True)
    spec_sub_subbands = models.TextField(blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    decl = models.FloatField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    equinox = models.CharField(max_length=10, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    central_frequency = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    subbands = models.TextField(blank=True, null=True)
    measurement_type = models.CharField(max_length=20)
    maximize_duration = models.IntegerField(blank=True, null=True)
    spec_maximize_duration = models.IntegerField(blank=True, null=True)
    ocd = models.IntegerField(blank=True, null=True)
    spec_ocd = models.IntegerField(blank=True, null=True)
    flyseye = models.IntegerField(blank=True, null=True)
    tab_nr_rings = models.IntegerField(blank=True, null=True)
    tab_ring_size = models.FloatField(blank=True, null=True)
    spec_flyseye = models.IntegerField(blank=True, null=True)
    spec_tab_nr_rings = models.IntegerField(blank=True, null=True)
    spec_tab_ring_size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_beam_measurement'


class LofarCalibrationPipeline(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    skymodel = models.CharField(max_length=50, blank=True, null=True)
    zerophase = models.IntegerField(blank=True, null=True)
    flagging_strategy = models.CharField(max_length=50, blank=True, null=True)
    frequency_integration_step = models.IntegerField(blank=True, null=True)
    time_integration_step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_calibration_pipeline'


class LofarCluster(models.Model):
    mom2objectid = models.IntegerField(blank=True, null=True)
    used_for = models.CharField(max_length=20, blank=True, null=True)
    cluster_name = models.CharField(max_length=20, blank=True, null=True)
    cluster_partition = models.CharField(max_length=80, blank=True, null=True)
    nr_of_tasks = models.IntegerField(blank=True, null=True)
    nr_of_cores_per_task = models.IntegerField(blank=True, null=True)
    min_ram_per_task = models.FloatField(blank=True, null=True)
    min_scratch_per_task = models.FloatField(blank=True, null=True)
    max_duration_per_task = models.FloatField(blank=True, null=True)
    run_simultaneous = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_cluster'


class LofarDataproduct(models.Model):
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)
    mom2_dp_id = models.IntegerField()
    storage_ticket = models.CharField(max_length=255, blank=True, null=True)
    filesize = models.BigIntegerField(blank=True, null=True)
    subband = models.IntegerField(blank=True, null=True)
    subband_index = models.IntegerField(blank=True, null=True)
    central_frequency = models.FloatField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    channel_width = models.FloatField(blank=True, null=True)
    number_of_channels = models.IntegerField(blank=True, null=True)
    integration_interval = models.FloatField(blank=True, null=True)
    sap = models.IntegerField(db_column='SAP', blank=True, null=True)  # Field name made lowercase.
    index_in_parset = models.IntegerField(blank=True, null=True)
    percentage_written = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    archive_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_dataproduct'


class LofarDataproductChecksum(models.Model):
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)
    algorithm = models.CharField(max_length=15, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_dataproduct_checksum'


class LofarDemixingParameters(models.Model):
    lofar_pipeline_id = models.IntegerField(blank=True, null=True)
    demix_freqstep = models.IntegerField(blank=True, null=True)
    demix_timestep = models.IntegerField(blank=True, null=True)
    averager_freqstep = models.IntegerField(blank=True, null=True)
    averager_timestep = models.IntegerField(blank=True, null=True)
    ignore_target = models.IntegerField(blank=True, null=True)
    demix_always = models.CharField(max_length=255, blank=True, null=True)
    demix_if_needed = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_demixing_parameters'


class LofarFolder(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid')
    contains_aborted_pipelines = models.IntegerField(blank=True, null=True)
    contains_finished_pipelines = models.IntegerField(blank=True, null=True)
    contains_aborted_observations = models.IntegerField(blank=True, null=True)
    contains_finished_observations = models.IntegerField(blank=True, null=True)
    contains_calibrators = models.IntegerField(blank=True, null=True)
    contains_targets = models.IntegerField(blank=True, null=True)
    extra_feedback = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_folder'


class LofarGenericMeasurement(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    spec_duration = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_generic_measurement'


class LofarImagingParameters(models.Model):
    lofar_pipeline_id = models.IntegerField(blank=True, null=True)
    field_of_view = models.FloatField(blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    robust = models.FloatField(blank=True, null=True)
    iterations = models.IntegerField(blank=True, null=True)
    threshold = models.CharField(max_length=20, blank=True, null=True)
    uv_min = models.FloatField(blank=True, null=True)
    uv_max = models.FloatField(blank=True, null=True)
    stokes = models.CharField(max_length=4, blank=True, null=True)
    nr_of_slices = models.IntegerField(blank=True, null=True)
    subbands_per_image = models.IntegerField(blank=True, null=True)
    max_baseline = models.IntegerField(blank=True, null=True)
    specify_fov = models.IntegerField(blank=True, null=True)
    cellsize = models.CharField(max_length=20, blank=True, null=True)
    npix = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_imaging_parameters'


class LofarImagingPipeline(models.Model):
    mom2objectid = models.IntegerField(blank=True, null=True)
    nr_of_slices = models.IntegerField(blank=True, null=True)
    subbands_per_image = models.IntegerField(blank=True, null=True)
    imaging_parameters_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_imaging_pipeline'


class LofarImagingPipelineMsss(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    imaging_parameters = models.ForeignKey(LofarImagingParameters, models.DO_NOTHING, blank=True, null=True)
    nr_of_slices = models.IntegerField(blank=True, null=True)
    subbands_per_image = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_imaging_pipeline_msss'


class LofarLocation(models.Model):
    name = models.CharField(max_length=15)
    coordinate_system = models.CharField(max_length=8, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    coordinates_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_location'


class LofarLongBaselinePipeline(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    subbands_per_subbandgroup = models.IntegerField(blank=True, null=True)
    subbandgroups_per_ms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_long_baseline_pipeline'


class LofarObservation(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    observation_id = models.IntegerField(blank=True, null=True)
    instrument = models.CharField(max_length=32, blank=True, null=True)
    user_specification = models.ForeignKey('LofarObservationSpecification', models.DO_NOTHING, blank=True, null=True, related_name='user_specs')
    system_specification = models.ForeignKey('LofarObservationSpecification', models.DO_NOTHING, blank=True, null=True, related_name='system_specs')
    default_template = models.CharField(max_length=50, blank=True, null=True)
    tbb_template = models.CharField(max_length=50, blank=True, null=True)
    tbb_piggyback_allowed = models.IntegerField()
    parset = models.TextField(blank=True, null=True)
    nr_output_correlated = models.IntegerField(blank=True, null=True)
    nr_output_beamformed = models.IntegerField(blank=True, null=True)
    nr_output_coherent_stokes = models.IntegerField(blank=True, null=True)
    nr_output_incoherent_stokes = models.IntegerField(blank=True, null=True)
    nr_output_flyseye = models.IntegerField(blank=True, null=True)
    nr_output_correlated_valid = models.IntegerField(blank=True, null=True)
    nr_output_beamformed_valid = models.IntegerField(blank=True, null=True)
    nr_output_coherent_stokes_valid = models.IntegerField(blank=True, null=True)
    nr_output_incoherent_stokes_valid = models.IntegerField(blank=True, null=True)
    nr_output_flyseye_valid = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    aartfaac_piggyback_allowed = models.TextField(blank=True, null=True)  # This field type is a guess.
    storage_cluster_id = models.IntegerField(blank=True, null=True)
    processing_cluster_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_observation'


class LofarObservationSpecification(models.Model):
    type = models.CharField(max_length=8, blank=True, null=True)
    correlated_data = models.IntegerField(blank=True, null=True)
    filtered_data = models.IntegerField(blank=True, null=True)
    beamformed_data = models.IntegerField(blank=True, null=True)
    coherent_stokes_data = models.IntegerField(blank=True, null=True)
    incoherent_stokes_data = models.IntegerField(blank=True, null=True)
    antenna = models.CharField(max_length=20, blank=True, null=True)
    clock_mode = models.CharField(max_length=10, blank=True, null=True)
    instrument_filter = models.CharField(max_length=15, blank=True, null=True)
    integration_interval = models.FloatField(blank=True, null=True)
    channels_per_subband = models.IntegerField(blank=True, null=True)
    cn_integration_steps = models.IntegerField(blank=True, null=True)
    pencilbeams_flyseye = models.IntegerField(blank=True, null=True)
    pencilbeams_nr_pencil_rings = models.IntegerField(blank=True, null=True)
    pencilbeams_ring_size = models.FloatField(blank=True, null=True)
    stokes_selection = models.CharField(max_length=4, blank=True, null=True)
    stokes_integrate_channels = models.IntegerField(blank=True, null=True)
    stokes_integration_steps = models.IntegerField(blank=True, null=True)
    station_set = models.CharField(max_length=15, blank=True, null=True)
    timeframe = models.CharField(max_length=4, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    spec_duration = models.FloatField(blank=True, null=True)
    coherent_dedisperse_channels = models.IntegerField(blank=True, null=True)
    dispersion_measure = models.FloatField(blank=True, null=True)
    subbands_per_file_cs = models.IntegerField(blank=True, null=True)
    subbands_per_file_bf = models.IntegerField(blank=True, null=True)
    collapsed_channels_cs = models.IntegerField(blank=True, null=True)
    collapsed_channels_is = models.IntegerField(blank=True, null=True)
    downsampling_steps_cs = models.IntegerField(blank=True, null=True)
    downsampling_steps_is = models.IntegerField(blank=True, null=True)
    which_cs = models.CharField(max_length=4, blank=True, null=True)
    which_is = models.CharField(max_length=4, blank=True, null=True)
    bypass_pff = models.IntegerField(blank=True, null=True)
    enable_superterp = models.IntegerField(blank=True, null=True)
    flyseye = models.IntegerField(blank=True, null=True)
    tab_nr_rings = models.IntegerField(blank=True, null=True)
    tab_ring_size = models.FloatField(blank=True, null=True)
    bits_per_sample = models.IntegerField(blank=True, null=True)
    misc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_observation_specification'


class LofarPencilbeam(models.Model):
    specificationid = models.ForeignKey(LofarObservationSpecification, models.DO_NOTHING, db_column='specificationid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    angle1 = models.FloatField(blank=True, null=True)
    angle2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_pencilbeam'


class LofarPipeline(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    pipeline_id = models.IntegerField(blank=True, null=True)
    pending = models.IntegerField(blank=True, null=True)
    template = models.CharField(max_length=100, blank=True, null=True)
    parset = models.TextField(blank=True, null=True)
    nr_output_correlated = models.IntegerField(blank=True, null=True)
    nr_output_beamformed = models.IntegerField(blank=True, null=True)
    nr_output_instrument_model = models.IntegerField(blank=True, null=True)
    nr_output_skyimage = models.IntegerField(blank=True, null=True)
    nr_output_correlated_valid = models.IntegerField(blank=True, null=True)
    nr_output_beamformed_valid = models.IntegerField(blank=True, null=True)
    nr_output_instrument_model_valid = models.IntegerField(blank=True, null=True)
    nr_output_skyimage_valid = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    demixing_parameters = models.ForeignKey(LofarDemixingParameters, models.DO_NOTHING, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    bbs_parameters_id = models.IntegerField(blank=True, null=True)
    storage_cluster_id = models.IntegerField(blank=True, null=True)
    processing_cluster_id = models.IntegerField(blank=True, null=True)
    misc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_pipeline'


class LofarPulsarPipeline(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    field_2bf2fits_extra_opts = models.CharField(db_column='_2bf2fits_extra_opts', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    field_8bit_conversion_sigma = models.FloatField(db_column='_8bit_conversion_sigma', blank=True, null=True)  # Field renamed because it started with '_'.
    decode_nblocks = models.IntegerField(blank=True, null=True)
    decode_sigma = models.IntegerField(blank=True, null=True)
    digifil_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    dspsr_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    dynamic_spectrum_time_average = models.FloatField(blank=True, null=True)
    nofold = models.IntegerField(blank=True, null=True)
    nopdmp = models.IntegerField(blank=True, null=True)
    norfi = models.IntegerField(blank=True, null=True)
    prepdata_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    prepfold_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    prepsubband_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    pulsar = models.CharField(max_length=100, blank=True, null=True)
    raw_to_8bit = models.IntegerField(blank=True, null=True)
    rfifind_extra_opts = models.CharField(max_length=100, blank=True, null=True)
    rrats = models.IntegerField(blank=True, null=True)
    single_pulse = models.IntegerField(blank=True, null=True)
    skip_dsps = models.IntegerField(blank=True, null=True)
    skip_dynamic_spectrum = models.IntegerField(blank=True, null=True)
    skip_prepfold = models.IntegerField(blank=True, null=True)
    tsubint = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_pulsar_pipeline'


class LofarSasDefaulttemplates(models.Model):
    sas_id = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    process_type = models.CharField(max_length=50, blank=True, null=True)
    sub_process_type = models.CharField(max_length=50, blank=True, null=True)
    strategy = models.CharField(max_length=100, blank=True, null=True)
    defaults = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_sas_defaulttemplates'


class LofarSpecificationStation(models.Model):
    specificationid = models.ForeignKey(LofarObservationSpecification, models.DO_NOTHING, db_column='specificationid', blank=True, null=True)
    stationid = models.ForeignKey('LofarStation', models.DO_NOTHING, db_column='stationid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_specification_station'


class LofarStation(models.Model):
    name = models.CharField(max_length=5)
    station_type = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_station'


class LofarTask(models.Model):
    processing = models.IntegerField(blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    mom2objectid = models.IntegerField(blank=True, null=True)
    attempt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_task'


class LofarTbbMeasurement(models.Model):
    mom2objectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    spec_duration = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_tbb_measurement'


class LofarTiedarraybeam(models.Model):
    specificationid = models.ForeignKey(LofarObservationSpecification, models.DO_NOTHING, db_column='specificationid', blank=True, null=True)
    mom2objectid = models.IntegerField(blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    usr_tab_flyseye = models.IntegerField(blank=True, null=True)
    usr_angle1 = models.FloatField(blank=True, null=True)
    usr_angle2 = models.FloatField(blank=True, null=True)
    usr_dm = models.FloatField(blank=True, null=True)
    sys_tab_flyseye = models.IntegerField(blank=True, null=True)
    sys_angle1 = models.FloatField(blank=True, null=True)
    sys_angle2 = models.FloatField(blank=True, null=True)
    sys_dm = models.FloatField(blank=True, null=True)
    usr_coherent = models.IntegerField(blank=True, null=True)
    sys_coherent = models.IntegerField(blank=True, null=True)
    absolute_angles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lofar_tiedarraybeam'




class LtaProject(models.Model):
    id = models.BigAutoField(primary_key=True)
    projectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='projectid')

    class Meta:
        managed = False
        db_table = 'lta_project'


class Member(models.Model):
    projectid = models.ForeignKey('Mom2Object', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Memberprojectrole(models.Model):
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    projectroleid = models.ForeignKey('Projectrole', models.DO_NOTHING, db_column='projectroleid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memberprojectrole'


class Mom2Id(models.Model):
    lastassignedmom2id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mom2id'


class Mom2Object(models.Model):
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='parentid', blank=True, null=True, related_name='parent_id')
    indexid = models.IntegerField(blank=True, null=True)
    mom2id = models.IntegerField(unique=True)
    mom2objecttype = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    ownerprojectid = models.ForeignKey('self', models.DO_NOTHING, db_column='ownerprojectid', blank=True, null=True, related_name='owner_project_id')
    currentstatusid = models.ForeignKey('Mom2Objectstatus', models.DO_NOTHING, db_column='currentstatusid', blank=True, null=True)
    topology = models.CharField(max_length=100, blank=True, null=True)
    predecessor = models.CharField(max_length=512, blank=True, null=True)
    topology_parent = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    datasize = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mom2object'

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ('+self.mom2objecttype+')'

class Mom2Objectdataproduct(models.Model):
    mom2objectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mom2objectdataproduct'


class Mom2Objectdataproductreference(models.Model):
    mom2objectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    dataproductid = models.ForeignKey(Dataproduct, models.DO_NOTHING, db_column='dataproductid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mom2objectdataproductreference'


class Mom2Objectstatus(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    roles = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusid', blank=True, null=True)
    mom2objectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)
    statustime = models.DateTimeField()
    pending = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mom2objectstatus'


class Mom2Objecttext(models.Model):
    mom2objectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    type = models.CharField(max_length=20)
    indexid = models.IntegerField(blank=True, null=True)
    textid = models.ForeignKey('Text', models.DO_NOTHING, db_column='textid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mom2objecttext'


class Nonregisteredmember(models.Model):
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nonregisteredmember'


class Project(models.Model):
    mom2objectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='mom2objectid', blank=True, null=True)
    releasedate = models.DateField(blank=True, null=True)
    allowtriggers = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project'


class Projectrole(models.Model):
    name = models.CharField(unique=True, max_length=15)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projectrole'


class Reference(models.Model):
    referencefromid = models.IntegerField(blank=True, null=True)
    referencetoid = models.IntegerField(blank=True, null=True)
    indexid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference'


class Registeredmember(models.Model):
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registeredmember'


class Resource(models.Model):
    projectid = models.ForeignKey(Mom2Object, models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    resourcetypeid = models.ForeignKey('Resourcetype', models.DO_NOTHING, db_column='resourcetypeid')
    allocation = models.FloatField(blank=True, null=True)
    used = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=20)
    projectpath = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource'


class ResourcesAllocatedSize(models.Model):
    mom2objectid = models.IntegerField()
    allocated_size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resources_allocated_size'


class Resourcetype(models.Model):
    name = models.CharField(max_length=255)
    hosturi = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'resourcetype'


class Status(models.Model):
    code = models.CharField(max_length=15)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'
        unique_together = (('code', 'type'),)


class Text(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    roles = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'text'


class Tmp(models.Model):
    mom2objectid = models.IntegerField(blank=True, null=True)
    observation_id = models.IntegerField(blank=True, null=True)
    instrument = models.CharField(max_length=32, blank=True, null=True)
    user_specification_id = models.IntegerField(blank=True, null=True)
    system_specification_id = models.IntegerField(blank=True, null=True)
    template = models.CharField(max_length=32, blank=True, null=True)
    default_template = models.CharField(max_length=50, blank=True, null=True)
    tbb_template = models.CharField(max_length=50, blank=True, null=True)
    tbb_piggyback_allowed = models.IntegerField(blank=True, null=True)
    parset = models.TextField(blank=True, null=True)
    nr_output_correlated = models.IntegerField(blank=True, null=True)
    nr_output_beamformed = models.IntegerField(blank=True, null=True)
    nr_output_coherent_stokes = models.IntegerField(blank=True, null=True)
    nr_output_incoherent_stokes = models.IntegerField(blank=True, null=True)
    nr_output_flyseye = models.IntegerField(blank=True, null=True)
    nr_output_correlated_valid = models.IntegerField(blank=True, null=True)
    nr_output_beamformed_valid = models.IntegerField(blank=True, null=True)
    nr_output_coherent_stokes_valid = models.IntegerField(blank=True, null=True)
    nr_output_incoherent_stokes_valid = models.IntegerField(blank=True, null=True)
    nr_output_flyseye_valid = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    aartfaac_piggyback_allowed = models.TextField(blank=True, null=True)  # This field type is a guess.
    storage_cluster_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp'
