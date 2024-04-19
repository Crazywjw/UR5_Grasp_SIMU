// Generated by gencpp from file household_objects_database_msgs/TranslateRecognitionIdResponse.msg
// DO NOT EDIT!


#ifndef HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_TRANSLATERECOGNITIONIDRESPONSE_H
#define HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_TRANSLATERECOGNITIONIDRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace household_objects_database_msgs
{
template <class ContainerAllocator>
struct TranslateRecognitionIdResponse_
{
  typedef TranslateRecognitionIdResponse_<ContainerAllocator> Type;

  TranslateRecognitionIdResponse_()
    : household_objects_id(0)
    , ID_NOT_FOUND(0)
    , DATABASE_ERROR(0)
    , OTHER_ERROR(0)
    , result(0)  {
    }
  TranslateRecognitionIdResponse_(const ContainerAllocator& _alloc)
    : household_objects_id(0)
    , ID_NOT_FOUND(0)
    , DATABASE_ERROR(0)
    , OTHER_ERROR(0)
    , result(0)  {
  (void)_alloc;
    }



   typedef int32_t _household_objects_id_type;
  _household_objects_id_type household_objects_id;

   typedef int32_t _ID_NOT_FOUND_type;
  _ID_NOT_FOUND_type ID_NOT_FOUND;

   typedef int32_t _DATABASE_ERROR_type;
  _DATABASE_ERROR_type DATABASE_ERROR;

   typedef int32_t _OTHER_ERROR_type;
  _OTHER_ERROR_type OTHER_ERROR;

   typedef int32_t _result_type;
  _result_type result;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(SUCCESS)
  #undef SUCCESS
#endif

  enum {
    SUCCESS = 0,
  };


  typedef boost::shared_ptr< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> const> ConstPtr;

}; // struct TranslateRecognitionIdResponse_

typedef ::household_objects_database_msgs::TranslateRecognitionIdResponse_<std::allocator<void> > TranslateRecognitionIdResponse;

typedef boost::shared_ptr< ::household_objects_database_msgs::TranslateRecognitionIdResponse > TranslateRecognitionIdResponsePtr;
typedef boost::shared_ptr< ::household_objects_database_msgs::TranslateRecognitionIdResponse const> TranslateRecognitionIdResponseConstPtr;

// constants requiring out of line definition

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator1> & lhs, const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator2> & rhs)
{
  return lhs.household_objects_id == rhs.household_objects_id &&
    lhs.ID_NOT_FOUND == rhs.ID_NOT_FOUND &&
    lhs.DATABASE_ERROR == rhs.DATABASE_ERROR &&
    lhs.OTHER_ERROR == rhs.OTHER_ERROR &&
    lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator1> & lhs, const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace household_objects_database_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b4afd505fbee150bf06acaffa82e84cf";
  }

  static const char* value(const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb4afd505fbee150bULL;
  static const uint64_t static_value2 = 0xf06acaffa82e84cfULL;
};

template<class ContainerAllocator>
struct DataType< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "household_objects_database_msgs/TranslateRecognitionIdResponse";
  }

  static const char* value(const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 household_objects_id\n"
"\n"
"int32 SUCCESS=0\n"
"int32 ID_NOT_FOUND\n"
"int32 DATABASE_ERROR\n"
"int32 OTHER_ERROR\n"
"int32 result\n"
"\n"
;
  }

  static const char* value(const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.household_objects_id);
      stream.next(m.ID_NOT_FOUND);
      stream.next(m.DATABASE_ERROR);
      stream.next(m.OTHER_ERROR);
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TranslateRecognitionIdResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::household_objects_database_msgs::TranslateRecognitionIdResponse_<ContainerAllocator>& v)
  {
    s << indent << "household_objects_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.household_objects_id);
    s << indent << "ID_NOT_FOUND: ";
    Printer<int32_t>::stream(s, indent + "  ", v.ID_NOT_FOUND);
    s << indent << "DATABASE_ERROR: ";
    Printer<int32_t>::stream(s, indent + "  ", v.DATABASE_ERROR);
    s << indent << "OTHER_ERROR: ";
    Printer<int32_t>::stream(s, indent + "  ", v.OTHER_ERROR);
    s << indent << "result: ";
    Printer<int32_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HOUSEHOLD_OBJECTS_DATABASE_MSGS_MESSAGE_TRANSLATERECOGNITIONIDRESPONSE_H
