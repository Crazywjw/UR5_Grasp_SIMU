# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from household_objects_database_msgs/GetModelListRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetModelListRequest(genpy.Message):
  _md5sum = "6bdf0a866151f41b8876e73800929933"
  _type = "household_objects_database_msgs/GetModelListRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# retrieves model id's from the database

# optional: the name of a model set that the id's should belong to;
# used to only retrieve a subset of models, pre-specified in the database
# leave empty to get all available models
string model_set

"""
  __slots__ = ['model_set']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       model_set

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetModelListRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.model_set is None:
        self.model_set = ''
    else:
      self.model_set = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.model_set
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_set = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_set = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.model_set
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_set = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_set = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from household_objects_database_msgs/GetModelListResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import household_objects_database_msgs.msg

class GetModelListResponse(genpy.Message):
  _md5sum = "81fac8c5d631e612bd9183a923572d53"
  _type = "household_objects_database_msgs/GetModelListResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
# the outcome of the query
DatabaseReturnCode return_code

# the actual model ids
int32[] model_ids

================================================================================
MSG: household_objects_database_msgs/DatabaseReturnCode
# return codes for database-related services

int32 UNKNOWN_ERROR = 1
int32 DATABASE_NOT_CONNECTED = 2
int32 DATABASE_QUERY_ERROR = 3
int32 SUCCESS = -1

int32 code"""
  __slots__ = ['return_code','model_ids']
  _slot_types = ['household_objects_database_msgs/DatabaseReturnCode','int32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       return_code,model_ids

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetModelListResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.return_code is None:
        self.return_code = household_objects_database_msgs.msg.DatabaseReturnCode()
      if self.model_ids is None:
        self.model_ids = []
    else:
      self.return_code = household_objects_database_msgs.msg.DatabaseReturnCode()
      self.model_ids = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.return_code.code
      buff.write(_get_struct_i().pack(_x))
      length = len(self.model_ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.model_ids))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.return_code is None:
        self.return_code = household_objects_database_msgs.msg.DatabaseReturnCode()
      end = 0
      start = end
      end += 4
      (self.return_code.code,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.model_ids = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.return_code.code
      buff.write(_get_struct_i().pack(_x))
      length = len(self.model_ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.model_ids.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.return_code is None:
        self.return_code = household_objects_database_msgs.msg.DatabaseReturnCode()
      end = 0
      start = end
      end += 4
      (self.return_code.code,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.model_ids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
class GetModelList(object):
  _type          = 'household_objects_database_msgs/GetModelList'
  _md5sum = '5f1f68d0a220da15352f6f1cb9a37fea'
  _request_class  = GetModelListRequest
  _response_class = GetModelListResponse
